# External Release Attestation — Claude V004 (ADR-0005 layer 2)

**Artifact:** IPBS-AUMNITY-SaaS-Tenant-Pilot_Claude_V004_20260809_0640.zip
**Final ZIP SHA-256:** `e86d73e7dc03a3f3a9b62c12862b4a8728ddfa1fd5cf6c1dcdb65f0890ae92b6`
**Build command:** `BUILD_TIMESTAMP=2026-08-09T06:40:00+01:00 python3 scripts/package_release.py <payload-tree> <out.zip>` (Python 3.12, ZIP_DEFLATED, sorted entries, fixed 0644 attrs)
**Payload:** 49 files (48 manifest-covered + PACKAGE-MANIFEST.json itself). Zero excluded directories.

## Determinism (G11a)
```
build1=e86d73e7dc03a3f3a9b62c12862b4a8728ddfa1fd5cf6c1dcdb65f0890ae92b6
build2=e86d73e7dc03a3f3a9b62c12862b4a8728ddfa1fd5cf6c1dcdb65f0890ae92b6
DETERMINISM: PASS (byte-identical)
```

## Manifest validation over the exact final payload (G01)
MANIFEST VALIDATION: PASS (48 files: inventory exact, no duplicates, bytes and SHA-256 verified; zero excluded directories — all evidence inside the integrity boundary)

## Smoke over a clean extraction of the SHIPPED ZIP (G11b/G11c)
The full attack suite (positive simulation + 35 negatives) was re-run from the extraction of the artifact whose hash is above:
```
SMOKE over clean extraction of shipped ZIP sha256=e86d73e7dc03a3f3a9b62c12862b4a8728ddfa1fd5cf6c1dcdb65f0890ae92b6:
No errors detected in compressed data of /mnt/user-data/outputs/IPBS-AUMNITY-SaaS-Tenant-Pilot_Claude_V004_20260809_0640.zip.
workbook inventory derived: sheets=11 dv_objects=22 inline_lists=11 central_refs=7 central_taxonomies=8 formula_cells=1507 transaction_data_rows=0 instruction_rows=9 reference_rows=7 review_template_rows=8 non_transaction_constant_rows=24
starter package contract: PASS
REGISTER/DOCS CONSISTENCY: PASS — scope: 10 check groups (see docstring); 29 entries; owners CGWO=11, NEW-MODULE=1, PLATFORM=6, TENANT-IPBS=4, UNRESOLVED=3, URAIFLOW=4; statuses CLASSIFIED=25, PROPOSED=4; product-owned=21; lifecycle history enforced (61 events across 29 RPRs, state-skipping impossible); evidence semantics + external provenance enforced against 3 registry products; ADR matrix over 7 ADRs. PASS covers exactly the listed checks, nothing broader.
MANIFEST VALIDATION: PASS (48 files: inventory exact, no duplicates, bytes and SHA-256 verified; zero excluded directories — all evidence inside the integrity boundary)
RESULT: positive future-lifecycle simulation PASSED; negative tests 35/35 DETECTED (R=13/13 lifecycle-model, L=8/8 history, E=8/8 evidence-semantics, P=3/3 provenance, M=3/3 integrity)
```

## Verification procedure
1. `sha256sum` the ZIP → must equal the hash above (G11d).
2. Extract; `python3 scripts/validate_manifest.py` → 48-file integrity.
3. `python3 scripts/validate_register.py` → lifecycle history + evidence semantics + provenance.
4. `python3 scripts/run_negative_tests.py .` → expect: positive simulation PASSED; 35/35 DETECTED.
5. Rebuild with the build command → identical hash.

## Authenticity boundary (unchanged, per V003 review point 6 — deferred)
This attestation provides integrity linkage, not issuer authenticity. Release signing/CI provenance remains future release-governance, outside this pilot's scope.
