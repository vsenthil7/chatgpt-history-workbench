# External Release Attestation — Claude V005 (ADR-0005 layer 2)

**Artifact:** IPBS-AUMNITY-SaaS-Tenant-Pilot_Claude_V005_20260809_0716.zip
**Final ZIP SHA-256:** `fb89f740d6bfe0d8936895f8627ce8cb82c35d3803e50831f042a97e91d3c81d`
**Build command:** `BUILD_TIMESTAMP=2026-08-09T07:16:00+01:00 python3 scripts/package_release.py <payload-tree> <out.zip>` (Python 3.12, ZIP_DEFLATED, sorted entries, fixed 0644 attrs)
**Payload:** 52 files (51 manifest-covered + PACKAGE-MANIFEST.json itself). Zero excluded directories.

## Determinism (G11a)
```
build1=fb89f740d6bfe0d8936895f8627ce8cb82c35d3803e50831f042a97e91d3c81d
build2=fb89f740d6bfe0d8936895f8627ce8cb82c35d3803e50831f042a97e91d3c81d
DETERMINISM: PASS (byte-identical)
```

## Manifest validation over the exact final payload (G01)
MANIFEST VALIDATION: PASS (51 files: inventory exact, no duplicates, bytes and SHA-256 verified; zero excluded directories — all evidence inside the integrity boundary)

## Smoke over a clean extraction of the SHIPPED ZIP (G11b/G11c)
Full attack suite (2 positive simulations + 51 negatives) re-run from the extraction of the artifact whose hash is above:
```
SMOKE over clean extraction of shipped ZIP sha256=fb89f740d6bfe0d8936895f8627ce8cb82c35d3803e50831f042a97e91d3c81d:
No errors detected in compressed data of /mnt/user-data/outputs/IPBS-AUMNITY-SaaS-Tenant-Pilot_Claude_V005_20260809_0716.zip.
workbook inventory derived: sheets=11 dv_objects=22 inline_lists=11 central_refs=7 central_taxonomies=8 formula_cells=1507 transaction_data_rows=0 instruction_rows=9 reference_rows=7 review_template_rows=8 non_transaction_constant_rows=24
starter package contract: PASS
REGISTER/DOCS CONSISTENCY: PASS — scope: 10 check groups (see docstring); 29 entries; owners CGWO=11, NEW-MODULE=1, PLATFORM=6, TENANT-IPBS=4, UNRESOLVED=3, URAIFLOW=4; statuses CLASSIFIED=25, PROPOSED=4; product-owned=21; lifecycle history enforced as UTC instants (61 events across 29 RPRs, state-skipping and offset-inversion impossible); tenant-bound (IPBS) evidence semantics with real ISO dates, temporal policy and external provenance against 3 ADR-approved registry products (STARTER abolished); ADR matrix over 8 ADRs. PASS covers exactly the listed checks, nothing broader.
MANIFEST VALIDATION: PASS (51 files: inventory exact, no duplicates, bytes and SHA-256 verified; zero excluded directories — all evidence inside the integrity boundary)
RESULT: positive simulations 2/2 PASSED (P0 future lifecycle; G4 ADR-approved new product); negative tests 51/51 DETECTED (R=13/13 model, L=8/8 history, E=8/8 evidence-semantics, P=3/3 provenance, T=4/4 tenant, D=4/4 dates, Z=1/1 instant-chronology, TE=3/3 temporal-policy, G=3/3 registry-authority, A=1/1 actor, M=3/3 integrity)
```

## Verification procedure
1. `sha256sum` the ZIP → hash above. 2. Extract; `validate_manifest.py` → 51-file integrity. 3. `validate_register.py` → tenant/time/temporal/registry enforcement. 4. `run_negative_tests.py .` → expect 2/2 positive, 51/51 DETECTED. 5. Rebuild with the command above → identical hash.

## Authenticity boundary (unchanged; ADR-0005 / ADR-0007 V005 amendment)
Integrity linkage only; issuer authenticity and cross-release non-repudiation remain deferred to release signing/CI provenance — outside this pilot's scope by review agreement.
