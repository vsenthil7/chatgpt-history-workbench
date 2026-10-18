# TalkProof — ConfigResolver test execution record
Date: 2026-10-04 (independent re-run during D-scale review response)
Environment: Python 3.12.3; PostgreSQL 16.15 local server; DATABASE_TEST_URL=postgresql://talkproof_app@localhost:5432/talkproof_test
Repository: talkproof-backend-master.zip (as supplied), services/api; requirements.txt installed as pinned
Command: pytest tests/unit/test_config_resolver.py tests/integration/test_config_resolver_acceptance.py --no-cov -o addopts="" -v -rA
Result: 24 passed, 0 failed, 0 skipped

Context run (same environment): pytest tests/unit tests/integration --no-cov -o addopts="" -q -> 1465 passed, 0 failed (155.88s), matching V5 Part 44 / E-01 §J.

## Verbatim pytest output (config resolver run)
```
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-8.3.4, pluggy-1.6.0 -- /usr/bin/python3
rootdir: /home/claude/tp/talkproof-backend-master/services/api
configfile: pytest.ini
plugins: anyio-4.15.1, cov-6.0.0, base-url-2.1.0, asyncio-0.25.0, playwright-0.7.0
asyncio: mode=Mode.AUTO, asyncio_default_fixture_loop_scope=None
collecting ... collected 24 items
tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_campaign_overrides_tenant_and_platform PASSED [  4%]
tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_tenant_overrides_platform_when_no_campaign_row PASSED [  8%]
tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_platform_used_when_no_tenant_or_campaign_row PASSED [ 12%]
tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_only_tenant_scope_resolves_tenant PASSED [ 16%]
tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_only_platform_scope_resolves_platform PASSED [ 20%]
tests/unit/test_config_resolver.py::TestGetEffectiveDefaults::test_missing_key_returns_default PASSED [ 25%]
tests/unit/test_config_resolver.py::TestGetEffectiveDefaults::test_missing_key_default_is_none PASSED [ 29%]
tests/unit/test_config_resolver.py::TestGetEffectiveExplicitNoneOverride::test_present_row_with_none_value_wins_over_lower_level PASSED [ 33%]
tests/unit/test_config_resolver.py::TestResolveSourceLevel::test_internal_resolve_reports_source PASSED [ 37%]
tests/unit/test_config_resolver.py::TestResolveSourceLevel::test_internal_resolve_reports_platform_and_default PASSED [ 41%]
tests/unit/test_config_resolver.py::TestFindCampaignConfigRepo::test_find_campaign_config_returns_row PASSED [ 45%]
tests/unit/test_config_resolver.py::TestFindCampaignConfigRepo::test_find_campaign_config_missing_returns_none PASSED [ 50%]
tests/unit/test_config_resolver.py::TestResolverCache::test_second_read_served_from_cache PASSED [ 54%]
tests/unit/test_config_resolver.py::TestResolverCache::test_invalidate_forces_reread PASSED [ 58%]
tests/unit/test_config_resolver.py::TestResolverCache::test_invalidate_all_clears_every_key PASSED [ 62%]
tests/unit/test_config_resolver.py::TestResolverCache::test_use_cache_false_bypasses_memo PASSED [ 66%]
tests/unit/test_config_resolver.py::TestResolverCache::test_cached_default_independent_of_value PASSED [ 70%]
tests/unit/test_config_resolver.py::TestResolveWithSource::test_returns_value_and_source_campaign PASSED [ 75%]
tests/unit/test_config_resolver.py::TestResolveWithSource::test_returns_default_source_for_missing PASSED [ 79%]
tests/unit/test_config_resolver.py::TestResolveWithSource::test_audit_off_writes_no_row PASSED [ 83%]
tests/unit/test_config_resolver.py::TestResolveWithSource::test_audit_on_writes_one_row PASSED [ 87%]
tests/unit/test_config_resolver.py::TestResolveWithSource::test_audit_records_default_level_for_missing PASSED [ 91%]
tests/integration/test_config_resolver_acceptance.py::TestM28Acceptance::test_full_precedence_default_and_audit PASSED [ 95%]
tests/integration/test_config_resolver_acceptance.py::TestM28Acceptance::test_source_levels_distinct PASSED [100%]
=============================== warnings summary ===============================
    _PortalFactoryType = typing.Callable[[], typing.ContextManager[anyio.abc.BlockingPortal]]
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_campaign_overrides_tenant_and_platform
PASSED tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_tenant_overrides_platform_when_no_campaign_row
PASSED tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_platform_used_when_no_tenant_or_campaign_row
PASSED tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_only_tenant_scope_resolves_tenant
PASSED tests/unit/test_config_resolver.py::TestGetEffectivePrecedence::test_only_platform_scope_resolves_platform
PASSED tests/unit/test_config_resolver.py::TestGetEffectiveDefaults::test_missing_key_returns_default
PASSED tests/unit/test_config_resolver.py::TestGetEffectiveDefaults::test_missing_key_default_is_none
PASSED tests/unit/test_config_resolver.py::TestGetEffectiveExplicitNoneOverride::test_present_row_with_none_value_wins_over_lower_level
PASSED tests/unit/test_config_resolver.py::TestResolveSourceLevel::test_internal_resolve_reports_source
PASSED tests/unit/test_config_resolver.py::TestResolveSourceLevel::test_internal_resolve_reports_platform_and_default
PASSED tests/unit/test_config_resolver.py::TestFindCampaignConfigRepo::test_find_campaign_config_returns_row
PASSED tests/unit/test_config_resolver.py::TestFindCampaignConfigRepo::test_find_campaign_config_missing_returns_none
PASSED tests/unit/test_config_resolver.py::TestResolverCache::test_second_read_served_from_cache
PASSED tests/unit/test_config_resolver.py::TestResolverCache::test_invalidate_forces_reread
PASSED tests/unit/test_config_resolver.py::TestResolverCache::test_invalidate_all_clears_every_key
PASSED tests/unit/test_config_resolver.py::TestResolverCache::test_use_cache_false_bypasses_memo
PASSED tests/unit/test_config_resolver.py::TestResolverCache::test_cached_default_independent_of_value
PASSED tests/unit/test_config_resolver.py::TestResolveWithSource::test_returns_value_and_source_campaign
PASSED tests/unit/test_config_resolver.py::TestResolveWithSource::test_returns_default_source_for_missing
PASSED tests/unit/test_config_resolver.py::TestResolveWithSource::test_audit_off_writes_no_row
PASSED tests/unit/test_config_resolver.py::TestResolveWithSource::test_audit_on_writes_one_row
PASSED tests/unit/test_config_resolver.py::TestResolveWithSource::test_audit_records_default_level_for_missing
PASSED tests/integration/test_config_resolver_acceptance.py::TestM28Acceptance::test_full_precedence_default_and_audit
PASSED tests/integration/test_config_resolver_acceptance.py::TestM28Acceptance::test_source_levels_distinct
======================== 24 passed, 4 warnings in 0.65s ========================
```
