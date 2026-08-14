import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        doc = item.function.__doc__
        if doc:
            report.longrepr = f"  Hint: {doc.strip()}"
