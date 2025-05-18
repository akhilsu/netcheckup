import socket
import subprocess
import platform
import time
import json
import speedtest


def dns_check(domains=["google.com", "cloudflare.com"]):
    """
    Perform DNS resolution for one or more domain names.

    Parameters:
    - domains (list): A list of domain names to resolve. Defaults to ["google.com", "cloudflare.com"].

    Returns:
    - dict: A dictionary with domain names as keys and their resolved IPs and resolution times in ms.
    """
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
    """
    Ping one or more hosts to check their network reachability.

    Parameters:
    - hosts (list): A list of host IPs or domain names to ping. Defaults to ["8.8.8.8", "1.1.1.1"].
    - count (int): Number of ping packets to send. Default is 3.

    Returns:
    - dict: A dictionary with hosts as keys and their ping status/output.
    """
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
    """
    Check if specific ports are open on a given host.

    Parameters:
    - host (str): Hostname or IP address to check. Default is "8.8.8.8".
    - ports (list): List of port numbers to check. Default is [53, 80, 443].

    Returns:
    - dict: A dictionary with port numbers as keys and "open"/"closed" as values.
    """
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
    """
    Run all default checks: DNS resolution, ping, and port availability.

    Returns:
    - dict: A combined dictionary containing all check results.
    """
    return {
        "dns_check": dns_check(),
        "ping_check": ping_check(),
        "port_check": port_check(),
        "speed_check": speed_check()
    }


def speed_check():
    """
    Check internet download and upload speeds using speedtest.net servers.

    Returns:
        dict: Contains download and upload speeds in Mbps, and ping in ms.
    """
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = round(st.download() / 1_000_000, 2)  # Mbps
        upload = round(st.upload() / 1_000_000, 2)      # Mbps
        ping = round(st.results.ping, 2)

        return {
            "download_mbps": download,
            "upload_mbps": upload,
            "ping_ms": ping
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print(json.dumps(run_all(), indent=2))
