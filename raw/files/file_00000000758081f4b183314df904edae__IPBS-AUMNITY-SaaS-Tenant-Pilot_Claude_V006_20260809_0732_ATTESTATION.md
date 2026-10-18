# External Release Attestation — Claude V006 (ADR-0005 layer 2) — ACCEPTANCE & FREEZE CANDIDATE

**Artifact:** IPBS-AUMNITY-SaaS-Tenant-Pilot_Claude_V006_20260809_0732.zip
**Final ZIP SHA-256:** `37d5bcc93b5fa9948dce31a9d08e8ffb1a8ee9731b4798d8966f56a92403ce43`
**Build command:** `BUILD_TIMESTAMP=2026-08-09T07:32:00+01:00 python3 scripts/package_release.py <payload-tree> <out.zip>` (Python 3.12, ZIP_DEFLATED, sorted entries, fixed 0644 attrs)
**Payload:** 54 files (53 manifest-covered + PACKAGE-MANIFEST.json itself). Zero excluded directories.
**Tenant trust anchor:** Pilot-tenant-id IPBS (ADR-0009, ACCEPTED) → TENANT-IDENTITY.json → evidence.

## Determinism (G11a)
```
build1=37d5bcc93b5fa9948dce31a9d08e8ffb1a8ee9731b4798d8966f56a92403ce43
build2=37d5bcc93b5fa9948dce31a9d08e8ffb1a8ee9731b4798d8966f56a92403ce43
DETERMINISM: PASS (byte-identical)
```

## Manifest validation over the exact final payload (G01)
MANIFEST VALIDATION: PASS (53 files: inventory exact, no duplicates, bytes and SHA-256 verified; zero excluded directories — all evidence inside the integrity boundary)

## Smoke over a clean extraction of the SHIPPED ZIP (G11b/G11c)
Full suite (3 positive simulations + 57 negatives across 13 categories) re-run from the extraction of the artifact whose hash is above:
```
SMOKE over clean extraction of shipped ZIP sha256=37d5bcc93b5fa9948dce31a9d08e8ffb1a8ee9731b4798d8966f56a92403ce43:
No errors detected in compressed data of /mnt/user-data/outputs/IPBS-AUMNITY-SaaS-Tenant-Pilot_Claude_V006_20260809_0732.zip.
workbook inventory derived: sheets=11 dv_objects=22 inline_lists=11 central_refs=7 central_taxonomies=8 formula_cells=1507 transaction_data_rows=0 instruction_rows=9 reference_rows=7 review_template_rows=8 non_transaction_constant_rows=24
starter package contract: PASS
REGISTER/DOCS CONSISTENCY: PASS — scope: 10 check groups (see docstring); 29 entries; owners CGWO=11, NEW-MODULE=1, PLATFORM=6, TENANT-IPBS=4, UNRESOLVED=3, URAIFLOW=4; statuses CLASSIFIED=25, PROPOSED=4; product-owned=21; lifecycle history enforced as UTC instants (61 events across 29 RPRs, state-skipping and offset-inversion impossible); tenant-bound (IPBS, anchored to ADR authority) evidence semantics with real ISO dates, temporal policy and external provenance against 3 ADR-approved registry products (STARTER abolished; active_from enforced); ADR matrix over 9 ADRs. PASS covers exactly the listed checks, nothing broader.
MANIFEST VALIDATION: PASS (53 files: inventory exact, no duplicates, bytes and SHA-256 verified; zero excluded directories — all evidence inside the integrity boundary)
RESULT: positive simulations 3/3 PASSED (P0 future lifecycle; G4 ADR-approved new product; TA5 display-name policy); negative tests 57/57 DETECTED (R=13/13 model, L=8/8 history, E=8/8 evidence-semantics, P=3/3 provenance, T=4/4 tenant, D=4/4 dates, Z=1/1 instant-chronology, TE=3/3 temporal-policy, G=3/3 registry-authority, TA=4/4 tenant-anchor, AF=2/2 active-from, A=1/1 actor, M=3/3 integrity)
```

## Verification procedure
1. `sha256sum` the ZIP → hash above. 2. Extract; `validate_manifest.py` → 53-file integrity. 3. `validate_register.py` → anchored-tenant/time/temporal/registry enforcement. 4. `run_negative_tests.py .` → expect 3/3 positive, 57/57 DETECTED. 5. Rebuild with the command above → identical hash.

## Authenticity boundary (unchanged)
Integrity linkage only; issuer authenticity/cross-release non-repudiation deferred to release signing/CI provenance — outside pilot scope by review agreement (ADR-0005; ADR-0007 V005 amendment).
