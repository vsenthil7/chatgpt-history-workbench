#!/usr/bin/env node
/**
 * Portfolio audit — the mechanical half of the review method that found 39 defects in
 * OnCall Copilot, 11 of them critical, nearly all invisible to a 100% coverage gate.
 *
 * v3 (20 September 2026) adds three checks from the Perplexity independent review V001:
 *   A10  enforcement/persistence method with no caller outside tests  (PX-002: claimWrite tested, checkWrite shipped)
 *   A11  boundary-crossing constructor argument absent from a named inventory (PX-003: response_url poster was console.log)
 *   A12  in-memory queue/buffer on a class not registered with the lifecycle (PX-004: ack queue lost on SIGTERM)
 * and one advisory pattern check, A13, for the "sync core, async world" class (PX-001).
 *
 * Repo-agnostic and read-only. Run from any Node/TypeScript product root:
 *   node audit.mjs [path-to-repo]
 *
 * It reports SUSPECTS, not verdicts: each finding is a place to look, with the question to
 * ask. The judgement stays human — that is deliberate, because the expensive defects were
 * all contract or integration mismatches that no checker can decide on its own.
 */
import { readdirSync, readFileSync, existsSync, statSync } from 'fs';
import { join, relative, extname, basename, resolve } from 'path';

// Absolute, so the directory-based classifiers (tests/, scripts/) work when run as `node audit.mjs .`.
const root = resolve(process.argv[2] ?? process.cwd());
const SRC_EXT = new Set(['.ts', '.tsx', '.js', '.mjs']);
const SKIP_DIR = new Set(['node_modules', '.git', 'dist', 'build', 'coverage', '.next']);

function walk(dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir)) {
    if (SKIP_DIR.has(name)) continue;
    const p = join(dir, name);
    const st = statSync(p);
    if (st.isDirectory()) walk(p, out);
    else out.push(p);
  }
  return out;
}

// The audit script and the playbook describe the patterns they search for; they must not audit themselves.
const files = walk(root).filter(f => !/(^|[\\/])(audit\.mjs|PORTFOLIO_AUDIT_PLAYBOOK\.md)$/.test(f));
const code = files.filter(f => SRC_EXT.has(extname(f)));
const isTest = f => /(^|[./])(test|spec)\.[jt]sx?$/.test(f) || /[\\/](tests?|__tests__)[\\/]/.test(f);
// Entry points are meant to have no importer — CLIs, configs and server shells.
const isEntry = f => /[\\/](scripts|bin|tools)[\\/]/.test(f) || /\.config\.[jt]s$/.test(f) || /[\\/]loadtest[\\/]/.test(f);
const srcFiles = code.filter(f => !isTest(f) && !isEntry(f));
const entryFiles = code.filter(f => !isTest(f) && isEntry(f));
const testFiles = code.filter(isTest);
const read = f => { try { return readFileSync(f, 'utf8'); } catch { return ''; } };
const rel = f => relative(root, f);

const findings = [];
const add = (id, severity, title, detail, question) => findings.push({ id, severity, title, detail, question });

// 1. Orphan modules — built but never called. Four of OnCall's criticals were this class.
const orphans = [];
for (const f of srcFiles) {
  const stem = basename(f, extname(f));
  if (/^(index|main|server|app)$/.test(stem)) continue;
  const importedBy = srcFiles.filter(o => o !== f && new RegExp(`from ['"][^'"]*${stem}['"]`).test(read(o)));
  const testedBy = testFiles.filter(o => new RegExp(`from ['"][^'"]*${stem}['"]`).test(read(o)));
  if (importedBy.length === 0) orphans.push({ file: rel(f), tested: testedBy.length > 0 });
}
if (orphans.length) {
  add('A1', orphans.some(o => o.tested) ? 'HIGH' : 'MEDIUM',
    `${orphans.length} module(s) with no importer outside tests`,
    orphans.map(o => `${o.file}${o.tested ? '  [has tests — fully covered and never called]' : ''}`).join('\n    '),
    'Is each of these a genuine library/CLI, or a feature nothing can reach? A tested-but-uncalled module passes every gate and does nothing in production.');
}

// 2. Published promises — claims in docs that need an enforcing line of code.
const docs = files.filter(f => extname(f) === '.md');
const PROMISES = [
  [/read[- ]only/i, 'Does any code path REFUSE a write when the account is read-only?'],
  [/\b\d+\s*[- ]day (retention|deletion)|delete[sd]? (your|all) data|retention policy/i, 'Is there a scheduled job that actually deletes, not just a flag or a date?'],
  [/encrypt(ed|ion) at rest/i, 'Does a write path call the encryption, or does the module merely exist?'],
  [/\b(per month|\/month|incidents|seats|messages|credits)\b.*\b(limit|included|up to)\b/i, 'Is the sold limit counted and refused at the cap?'],
  [/unlimited|no limits/i, 'Is "unlimited" actually unbounded in code, or will a cap surprise a customer?'],
  [/grace period|dunning/i, 'Does the grace period expire into an enforced state?'],
  [/SLA|within \d+ (business )?hours?/i, 'Is the SLA measured somewhere, or only promised?'],
  [/export (your|all) data|delete my data/i, 'Is there a route a user can actually call?']
];
const promiseHits = [];
for (const d of docs) {
  const text = read(d);
  for (const [re, question] of PROMISES) {
    if (re.test(text)) promiseHits.push(`${rel(d)} — ${question}`);
  }
}
if (promiseHits.length) {
  add('A2', 'HIGH', `${promiseHits.length} customer-facing promise(s) to trace to enforcing code`,
    [...new Set(promiseHits)].join('\n    '),
    'For each claim, name the line that refuses what the claim forbids. Two of OnCall\'s criticals were promises with no gate.');
}

// 3. Process-local state — breaks on restart and across replicas.
const stateHits = [];
for (const f of srcFiles) {
  const t = read(f);
  const m = t.match(/private\s+\w+\s*(:[^=]+)?=\s*(new (Map|Set)\(|\[\]|0\b)/g) ?? [];
  const counters = t.match(/\b(seq|sequence|counter|nextId)\b\s*(\+\+|\+=)/g) ?? [];
  if (m.length >= 2 || counters.length) {
    stateHits.push(`${rel(f)}  (${m.length} in-memory field(s)${counters.length ? ', increments a counter' : ''})`);
  }
}
if (stateHits.length) {
  add('A3', 'HIGH', `${stateHits.length} file(s) holding process-local state`,
    stateHits.slice(0, 25).join('\n    '),
    'What happens to this on restart, and what happens when two replicas run at once? A locally incremented id collided and OVERWROTE rows in OnCall — under blue/green specifically.');
}

// 4. Self-written DB fakes — circular evidence.
const fakeHits = testFiles.filter(f => /class\s+Fake(Pg|Db|Database)|mock(Pg|Db)|fakeQuery/i.test(read(f))).map(rel);
const realPg = testFiles.some(f => /pg-mem|DATABASE_URL_TEST|testcontainers/i.test(read(f)));
if (fakeHits.length && !realPg) {
  add('A4', 'HIGH', 'Database adapters proven only against a self-written fake',
    fakeHits.join('\n    '),
    'A fake written to match your own SQL agrees with whatever you wrote. Running the real migrations against pg-mem or a real Postgres found a critical foreign-key defect in OnCall that had been "contract-verified" for six sprints.');
}

// 5. Routes referenced in docs/config but not served anywhere.
const routeRefs = new Set();
for (const d of [...docs, ...files.filter(f => /\.(json|ya?ml)$/.test(f))]) {
  for (const m of read(d).matchAll(/["'`\s(](\/(?:api|slack|oauth|ops|webhook|health)[a-z0-9/_-]*)/gi)) routeRefs.add(m[1]);
}
const served = [...srcFiles, ...entryFiles].map(read).join('\n');
const missing = [...routeRefs].filter(r => !served.includes(r));
if (missing.length) {
  add('A5', 'CRITICAL', `${missing.length} route(s) referenced in docs/config but not found in code`,
    missing.join('\n    '),
    'Does an HTTP app actually serve these? OnCall had a manifest, a setup guide and a load script pointing at routes NOTHING served — the documented install path was impossible.');
}

// 6. Optional collaborators — the pattern that lets enforcement be skipped.
const optional = [];
for (const f of srcFiles) {
  for (const m of read(f).matchAll(/private\s+(\w*(?:writer|repo|repository|store|sink|crypto|meter|notifier|gate|entitlement)\w*)\??\s*[?:]/gi)) {
    if (/\?\s*:/.test(m[0]) || m[0].includes('?')) optional.push(`${rel(f)} — ${m[1]}`);
  }
}
if (optional.length) {
  add('A6', 'MEDIUM', `${optional.length} optional persistence/enforcement collaborator(s)`,
    [...new Set(optional)].slice(0, 20).join('\n    '),
    'Optional means someone can forget to wire it, and the tests still pass. Make persistence, crypto and entitlement gates REQUIRED constructor arguments.');
}

// 7. Coverage-gate presence (necessary, nowhere near sufficient).
const pkgPath = join(root, 'package.json');
const pkg = existsSync(pkgPath) ? JSON.parse(read(pkgPath)) : {};
const jestCfg = existsSync(join(root, 'jest.config.js')) ? read(join(root, 'jest.config.js')) : JSON.stringify(pkg.jest ?? {});
if (!/coverageThreshold/.test(jestCfg)) {
  add('A7', 'MEDIUM', 'No enforced coverage threshold found', 'jest.config / package.json',
    'A gate does not prove reachability, but its absence means regressions land silently.');
}

// 8. THE COMPOSITION ROOT OUTSIDE THE GATES — the class that made every other class invisible.
// OnCall Copilot's second review found ten blockers in scripts/serve.ts: a file that did not
// compile, wired eight in-memory stores in production, resolved every session to undefined and
// discarded every async response. 473 tests at 100% coverage were green the whole time, because
// tsconfig included src/** only and jest excluded scripts/. The gate did not cover the one file
// that decides what the deployed product is.
const tsconfigPath = join(root, 'tsconfig.json');
if (existsSync(tsconfigPath)) {
  // Tolerant parse: tsconfig routinely carries comments and trailing commas.
  const rawTs = read(tsconfigPath).replace(/\/\*[\s\S]*?\*\//g, '').replace(/^\s*\/\/.*$/gm, '').replace(/,(\s*[}\]])/g, '$1');
  let ts = {};
  try { ts = JSON.parse(rawTs); } catch { ts = {}; }
  const include = (ts.include ?? []).join(' ');
  const uncheckedEntries = entryFiles.filter(f => {
    // Only files the compiler would have checked: a k6 script or a jest config is not a
    // composition root and is meant to sit outside the build.
    if (!/\.tsx?$/.test(f) || /\.config\.[jt]s$/.test(f)) return false;
    const dir = rel(f).replace(/\\/g, '/').split('/')[0];
    return include.length > 0 && !include.includes(dir);
  });
  if (uncheckedEntries.length) {
    add('A8', 'CRITICAL',
      `${uncheckedEntries.length} entry point(s) outside the type-check`,
      uncheckedEntries.map(rel).join('\n    ') + `\n    tsconfig include: ${include || '(none)'}`,
      'Does your build actually compile the file that wires the product together? If tsconfig excludes it and no test imports it, a composition root that cannot start will pass every gate you have.');
  }
}
// The same blind spot from the test side: an entry point no test imports AND no coverage config
// collects from is a file whose correctness nothing checks.
const coverageFrom = /collectCoverageFrom[^\]]*\]/.exec(jestCfg)?.[0] ?? '';
const untestedEntries = entryFiles.filter(f => {
  const stem = basename(f, extname(f));
  const imported = testFiles.some(o => new RegExp(`from ['"][^'"]*${stem}['"]`).test(read(o)));
  const dir = rel(f).replace(/\\/g, '/').split('/')[0];
  return !imported && coverageFrom.length > 0 && !coverageFrom.includes(dir);
});
if (untestedEntries.length) {
  add('A9', 'HIGH',
    `${untestedEntries.length} entry point(s) neither imported by a test nor measured by coverage`,
    untestedEntries.map(rel).join('\n    '),
    'What proves this file works? Boot it in CI from the built artifact — a boot smoke test is the cheapest test you will ever write and it catches the most expensive class of defect.');
}

// 10. A10 — TWO ENFORCEMENT METHODS, ONE WIRED (PX-002). A method whose name says it enforces,
// persists or claims something, and whose only callers are tests, is an enforcement path the
// deployed product never takes. This is the highest-yield of the v3 checks: it would have found
// PX-002 mechanically — `claimWrite` was fully tested and called by nothing in src/ or scripts/.
const ENFORCE_RE = /\b(async\s+)?(claim\w*|enforce\w*|assert\w*|require\w*|refuse\w*|persist\w*|reencrypt\w*|rotate\w*|revoke\w*|drain\w*|flush\w*|purge\w*|acquire\w*)\s*\(/g;
const prodText = [...srcFiles, ...entryFiles].map(read).join('\n');
const testText = testFiles.map(read).join('\n');
const uncalledEnforcers = [];
for (const f of srcFiles) {
  const t = read(f);
  const seen = new Set();
  for (const m of t.matchAll(ENFORCE_RE)) {
    const name = m[2];
    if (seen.has(name) || /^(assertCan|require)$/.test(name)) continue;
    seen.add(name);
    // Declared here (method or function definition), called nowhere else in src/scripts, called in tests.
    const declaredHere = new RegExp(`(^|\\s)(async\\s+)?${name}\\s*\\(`, 'm').test(t);
    const callers = (prodText.match(new RegExp(`\\.${name}\\(`, 'g')) ?? []).length;
    const testCallers = (testText.match(new RegExp(`\\.${name}\\(`, 'g')) ?? []).length;
    if (declaredHere && callers === 0 && testCallers > 0) uncalledEnforcers.push(`${rel(f)} — ${name}()  [called ${testCallers}x in tests, 0x in src/scripts]`);
  }
}
if (uncalledEnforcers.length) {
  add('A10', 'CRITICAL', `${uncalledEnforcers.length} enforcement/persistence method(s) with no caller outside tests`,
    uncalledEnforcers.join('\n    '),
    'Which method does the DEPLOYED composition call? A tested, uncalled enforcement method means the product enforces something else — or nothing. Write a test that builds the production composition and asserts the enforcement outcome (OnCall: tests/px/enforcementWiring).');
}

// 11. A11 — GATE BY ENUMERATION (PX-003). A boot gate that checks a list of providers is only
// as complete as the list. Look for a required-providers inventory, then for constructor
// arguments / deps fields whose names or types say "crosses a process boundary" but which are
// not in that inventory.
const inventoryDecl = /(REQUIRED_PROVIDERS|REQUIRED_ADAPTERS|PROVIDER_KEYS|providerInventory)\s*=?\s*\[?([^;]*)/.exec(prodText);
if (inventoryDecl) {
  const inventoried = new Set([...(inventoryDecl[2].matchAll(/['"]([a-zA-Z]+)['"]/g))].map(m => m[1].toLowerCase()));
  const BOUNDARY_RE = /\b(\w*(?:poster|opener|client|adapter|provider|publisher|notifier|vault|oauth|payments|webhook|mailer|sender)\w*)\s*[?:]\s*(?:\(|[A-Z]\w*)/g;
  const missing = new Set();
  for (const f of [...srcFiles, ...entryFiles]) {
    if (/composition[\\/](providers|production|runtime)|core[\\/]provider/.test(f)) continue;
    for (const m of read(f).matchAll(BOUNDARY_RE)) {
      const field = m[1];
      if (/^(is|has|use|resolve|register)/i.test(field)) continue;
      const key = field.replace(/(Adapter|Client|Provider)$/i, '').toLowerCase();
      if (![...inventoried].some(k => key.includes(k) || k.includes(key))) missing.add(`${rel(f)} — ${field}`);
    }
  }
  if (missing.size) {
    add('A11', 'HIGH', `${missing.size} boundary-crossing dependency field(s) not obviously in the provider inventory`,
      [...missing].slice(0, 20).join('\n    '),
      'Is each of these constructed as a NAMED, health-checked provider that the boot gate probes? OnCall shipped a response_url poster as a console.log closure and views.open as a bare lambda — neither in REQUIRED_PROVIDERS, so a correctly-inventoried production boot would have sent every declare result to the container log.');
  }
} else {
  add('A11', 'MEDIUM', 'No named provider inventory found (REQUIRED_PROVIDERS / providerInventory)',
    'A boot gate that does not enumerate its providers cannot refuse a missing one.',
    'Add a closed, typed provider set whose inventory is derived from the constructed objects, and probe healthcheck() on each at boot.');
}

// 12. A12 — QUEUE WITHOUT A LIFECYCLE (PX-004). An in-memory queue or buffer field on a class
// that is not registered with a lifecycle/shutdown hook is work that dies with the process.
const lifecycleRegs = new Set([...prodText.matchAll(/lifecycle\.register\((\w+)\)/g)].map(m => m[1].toLowerCase()));
const queueOwners = [];
for (const f of srcFiles) {
  const t = read(f);
  const cls = /^\s*(?:export\s+)?(?:abstract\s+)?class\s+(\w+)/m.exec(t)?.[1];
  if (!cls) continue;
  const hasQueue = /private\s+(queue|buffer|pending|backlog|failed|replayQueue)\w*\s*(:[^=]+)?=\s*\[\]/.test(t);
  if (!hasQueue) continue;
  const drainable = /flush\s*\(\)\s*:\s*Promise|implements\s+\w*Drainable/.test(t);
  const instanceNames = [...prodText.matchAll(new RegExp(`(\\w+)\\s*=\\s*new\\s+${cls}\\(`, 'g'))].map(m => m[1].toLowerCase());
  const registered = instanceNames.some(n => lifecycleRegs.has(n));
  if (!registered) queueOwners.push(`${rel(f)} — class ${cls}${drainable ? ' (is Drainable but not registered)' : ' (no flush(): Promise / Drainable)'}`);
}
if (queueOwners.length) {
  add('A12', 'HIGH', `${queueOwners.length} class(es) holding an in-memory queue/buffer not registered with the lifecycle`,
    queueOwners.join('\n    '),
    'What happens to this queue on SIGTERM — every blue/green deploy? OnCall\'s slash-command ack queue was not drained at shutdown, so queued declares vanished after the user had been told "⏳ Declaring incident…". Register it, and persist it if a kill -9 must be survivable.');
}

// 13. A13 (advisory) — SYNC CORE, ASYNC WORLD (PX-001). Interfaces whose names say "platform"
// (client/provider/publisher/adapter/api) but whose methods return values rather than Promises
// can only ever be satisfied by stubs — the gate then proves the core agrees with its own fakes.
const syncPlatformIfaces = [];
for (const f of srcFiles) {
  const t = read(f);
  for (const m of t.matchAll(/export\s+interface\s+(\w*(?:Client|Provider|Publisher|Adapter|Api|Poster|Opener))\s*(?:extends[^{]*)?\{([^}]*)\}/g)) {
    const body = m[2];
    const methods = [...body.matchAll(/(\w+)\s*\([^)]*\)\s*:\s*([^;]+);/g)];
    const sync = methods.filter(x => !/^Promise</.test(x[2].trim())).map(x => x[1]);
    if (sync.length) syncPlatformIfaces.push(`${rel(f)} — ${m[1]}: ${sync.join(', ')}`);
  }
}
if (syncPlatformIfaces.length) {
  add('A13', 'HIGH', `${syncPlatformIfaces.length} platform-shaped interface(s) with synchronous methods`,
    syncPlatformIfaces.join('\n    '),
    'Can a real HTTP adapter satisfy this contract? If every method returns a value, only a stub can implement it, and every test above it is testing the stub. Convert the boundary BEFORE writing adapters (OnCall PX-S0), or the adapters sprint becomes a core-contract migration mid-sprint.');
}

const order = { CRITICAL: 0, HIGH: 1, MEDIUM: 2 };
findings.sort((a, b) => order[a.severity] - order[b.severity]);

console.log(`\nPortfolio audit v3 — ${rel(root) || root}`);
console.log(`${srcFiles.length} source files, ${entryFiles.length} entry points, ${testFiles.length} test files, ${docs.length} docs\n`);
if (!findings.length) {
  console.log('No mechanical suspects found. The judgement-based checks in the playbook still apply.\n');
} else {
  for (const f of findings) {
    console.log(`[${f.severity}] ${f.id}  ${f.title}`);
    console.log(`    ${f.detail}`);
    console.log(`  ? ${f.question}\n`);
  }
}
console.log(`${findings.length} area(s) to investigate. These are suspects, not verdicts.\n`);
process.exit(findings.some(f => f.severity === 'CRITICAL') ? 1 : 0);
