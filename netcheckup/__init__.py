from .core import run_all
import json

def main():
    result = run_all()
    print(json.dumps(result, indent=2))

from .core import dns_check, ping_check, port_check, run_all, speed_check

__all__ = ["dns_check", "ping_check", "port_check", "run_all", "speed_check"]
