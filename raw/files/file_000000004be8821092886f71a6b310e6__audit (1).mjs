#!/usr/bin/env node
/**
 * Portfolio audit — the mechanical half of the review method that found 39 defects in
 * OnCall Copilot, 11 of them critical, nearly all invisible to a 100% coverage gate.
 *
 * Repo-agnostic and read-only. Run from any Node/TypeScript product root:
 *   node audit.mjs [path-to-repo]
 *
 * It reports SUSPECTS, not verdicts: each finding is a place to look, with the question to
 * ask. The judgement stays human — that is deliberate, because the expensive defects were
 * all contract or integration mismatches that no checker can decide on its own.
 */
import { readdirSync, readFileSync, existsSync, statSync } from 'fs';
import { join, relative, extname, basename } from 'path';

const root = process.argv[2] ?? process.cwd();
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

const files = walk(root);
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
const served = srcFiles.map(read).join('\n');
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

const order = { CRITICAL: 0, HIGH: 1, MEDIUM: 2 };
findings.sort((a, b) => order[a.severity] - order[b.severity]);

console.log(`\nPortfolio audit — ${rel(root) || root}`);
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
