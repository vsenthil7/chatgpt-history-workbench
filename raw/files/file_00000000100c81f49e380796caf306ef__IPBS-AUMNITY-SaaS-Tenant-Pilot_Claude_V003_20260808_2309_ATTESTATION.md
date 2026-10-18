# External Release Attestation — Claude V003 (ADR-0005 layer 2)

**Artifact:** IPBS-AUMNITY-SaaS-Tenant-Pilot_Claude_V003_20260808_2309.zip
**Final ZIP SHA-256:** `15a4ca8b7d4a1d4c9658fc41bf681099a4f857f0fce21fb4fc1c316a2b822acb`
**Build command:** `BUILD_TIMESTAMP=2026-08-08T23:09:00+01:00 python3 scripts/package_release.py <payload-tree> <out.zip>` (Python 3.12, zipfile ZIP_DEFLATED, sorted entries, fixed 0644 attrs)
**Payload:** 45 files (44 manifest-covered + PACKAGE-MANIFEST.json itself). Zero excluded directories.

## Determinism (G11a)
Two successive builds of the frozen payload:
```
build1=15a4ca8b7d4a1d4c9658fc41bf681099a4f857f0fce21fb4fc1c316a2b822acb
build2=15a4ca8b7d4a1d4c9658fc41bf681099a4f857f0fce21fb4fc1c316a2b822acb
DETERMINISM: PASS (byte-identical)
```

## Manifest validation over the exact final payload (G01)
MANIFEST VALIDATION: PASS (44 files: inventory exact, no duplicates, bytes and SHA-256 verified; zero excluded directories — all evidence inside the integrity boundary)

## Smoke over a clean extraction of the SHIPPED ZIP (G11b/G11c)
Transcript (run from the extraction of the artifact whose hash is above — not a candidate tree):
```
SMOKE over clean extraction of shipped ZIP sha256=15a4ca8b7d4a1d4c9658fc41bf681099a4f857f0fce21fb4fc1c316a2b822acb:
No errors detected in compressed data of /mnt/user-data/outputs/IPBS-AUMNITY-SaaS-Tenant-Pilot_Claude_V003_20260808_2309.zip.
workbook inventory derived: sheets=11 dv_objects=22 inline_lists=11 central_refs=7 central_taxonomies=8 formula_cells=1507 transaction_data_rows=0 instruction_rows=9 reference_rows=7 review_template_rows=8 non_transaction_constant_rows=24
starter package contract: PASS
REGISTER/DOCS CONSISTENCY: PASS — scope: 10 check groups (see docstring); 29 entries; owners CGWO=11, NEW-MODULE=1, PLATFORM=6, TENANT-IPBS=4, UNRESOLVED=3, URAIFLOW=4; statuses CLASSIFIED=25, PROPOSED=4; product-owned=21; ADR matrix enforced over 6 ADRs (4 gated refs); structured evidence fully resolved. PASS covers exactly the listed checks, nothing broader.
MANIFEST VALIDATION: PASS (44 files: inventory exact, no duplicates, bytes and SHA-256 verified; zero excluded directories — all evidence inside the integrity boundary)
NEGATIVE TESTS: 16/16 DETECTED
```
Note: the smoke run re-executed derive_workbook_inventory.py inside the extraction and manifest validation still passed afterwards — the inventory regeneration is itself byte-deterministic.

## Verification procedure for any reviewer
1. `sha256sum` the ZIP → must equal the hash above (G11d).
2. Extract; run `python3 scripts/validate_manifest.py` → payload integrity, all files covered.
3. Run `python3 scripts/validate_register.py`, `validate_starter.py`, `run_negative_tests.py .`.
4. Rebuild with the build command above → identical hash.
