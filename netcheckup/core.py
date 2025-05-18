import socket
import subprocess
import platform
import time
import json


def dns_check(domains=["google.com", "cloudflare.com"]):
    results = {}
    for domain in domains:
        try:
            start = time.time()
            ip = socket.gethostbyname(domain)
            duration = round((time.time() - start) * 1000, 2)
            results[domain] = {"ip": ip, "time_ms": duration}
        except Exception as e:
            results[domain] = {"error": str(e)}
    return results


def ping_check(hosts=["8.8.8.8", "1.1.1.1"], count=3):
    results = {}
    param = "-n" if platform.system().lower() == "windows" else "-c"
    for host in hosts:
        try:
            cmd = ["ping", param, str(count), host]
            output = subprocess.check_output(cmd, universal_newlines=True)
            results[host] = {"status": "reachable", "output": output}
        except subprocess.CalledProcessError as e:
            results[host] = {"status": "unreachable", "error": str(e)}
    return results


def port_check(host="8.8.8.8", ports=[53, 80, 443]):
    results = {}
    for port in ports:
        try:
            sock = socket.create_connection((host, port), timeout=3)
            sock.close()
            results[port] = "open"
        except:
            results[port] = "closed"
    return results


def run_all():
    return {
        "dns_check": dns_check(),
        "ping_check": ping_check(),
        "port_check": port_check()
    }


if __name__ == "__main__":
    print(json.dumps(run_all(), indent=2))
