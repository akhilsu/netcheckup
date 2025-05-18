import argparse
from . import dns_check, ping_check, port_check, run_all, speed_check
import json

def main():
    parser = argparse.ArgumentParser(description="NetCheckup - Network Diagnostics CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add sub-commands
    subparsers.add_parser("all", help="Run all checks")
    subparsers.add_parser("dns", help="Run DNS check")
    subparsers.add_parser("ping", help="Run Ping check")
    subparsers.add_parser("port", help="Run Port check")
    subparsers.add_parser("speed", help="Run Speed check")

    args = parser.parse_args()

    if args.command == "all":
        print(json.dumps(run_all(), indent=2))
    elif args.command == "dns":
        print(json.dumps(dns_check(), indent=2))
    elif args.command == "ping":
        print(json.dumps(ping_check(), indent=2))
    elif args.command == "port":
        print(json.dumps(port_check(), indent=2))
    elif args.command == "speed":
        print(json.dumps(speed_check(), indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
