# tests/test_core.py

from netcheckup.core import dns_check, ping_check, port_check

def test_dns_check():
    result = dns_check(["google.com"])
    assert "google.com" in result
    assert "ip" in result["google.com"] or "error" in result["google.com"]

def test_ping_check():
    result = ping_check(["8.8.8.8"], count=1)
    assert "8.8.8.8" in result

def test_port_check():
    result = port_check("8.8.8.8", [53])
    assert 53 in result
