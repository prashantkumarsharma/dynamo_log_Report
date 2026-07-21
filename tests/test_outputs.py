import json

def load_report():
    with open("/app/report.json") as f:
        return json.load(f)

def test_success_criterion_1():
    """Success criterion 1: report.json exists and is valid JSON."""
    report = load_report()
    assert isinstance(report, dict)

def test_success_criterion_2():
    """Success criterion 2: total_requests is correct."""
    report = load_report()
    assert report["total_requests"] == 6

def test_success_criterion_3():
    """Success criterion 3: unique_ips is correct."""
    report = load_report()
    assert report["unique_ips"] == 3

def test_success_criterion_4():
    """Success criterion 4: top_path is correct."""
    report = load_report()
    assert report["top_path"] == "/index.html"