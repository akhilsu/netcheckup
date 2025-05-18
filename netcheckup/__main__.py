import argparse
from . import dns_check, ping_check, port_check, run_all, speed_check
import json

def main():
    parser = argparse.ArgumentParser(description="NetCheckup - Network Diagnostics CLI")
    subparsers = parser.add_subparsers(dest="command")

    # all
    subparsers.add_parser("all", help="Run all checks")

    # dns with optional --domain arguments (accept multiple)
    dns_parser = subparsers.add_parser("dns", help="Run DNS check")
    dns_parser.add_argument(
        '--domain', '-d',
        nargs='+',
        default=["google.com", "cloudflare.com"],
        help="Domain(s) to resolve"
    )

    # ping with optional --host(s) and --count
    ping_parser = subparsers.add_parser("ping", help="Run Ping check")
    ping_parser.add_argument(
        '--host', '-H',
        nargs='+',
        default=["8.8.8.8", "1.1.1.1"],
        help="Host(s) to ping"
    )
    ping_parser.add_argument(
        '--count', '-c',
        type=int,
        default=3,
        help="Number of ping packets"
    )

    # port with optional --host and --ports
    port_parser = subparsers.add_parser("port", help="Run Port check")
    port_parser.add_argument(
        '--host', '-H',
        default="8.8.8.8",
        help="Host to check ports on"
    )
    port_parser.add_argument(
        '--ports', '-p',
        nargs='+',
        type=int,
        default=[53, 80, 443],
        help="Ports to check"
    )

    # speed has no arguments
    subparsers.add_parser("speed", help="Run Speed check")

    args = parser.parse_args()

    if args.command == "all":
        print(json.dumps(run_all(), indent=2))

    elif args.command == "dns":
        print(json.dumps(dns_check(domains=args.domain), indent=2))

    elif args.command == "ping":
        print(json.dumps(ping_check(hosts=args.host, count=args.count), indent=2))

    elif args.command == "port":
        print(json.dumps(port_check(host=args.host, ports=args.ports), indent=2))

    elif args.command == "speed":
        print(json.dumps(speed_check(), indent=2))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
