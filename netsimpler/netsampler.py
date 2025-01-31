import argparse
import subprocess
import json

def run_command(command: list):
    """Execute a system command and return its output."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}"

def list_rules(ipv6: bool = False):
    """List all iptables rules for IPv4 or IPv6."""
    cmd = ["sudo", "ip6tables" if ipv6 else "iptables", "-L", "-v", "-n"]
    return run_command(cmd)

def add_rule(chain: str, protocol: str, port: str, action: str, source: str = None, dest: str = None, log: bool = False, ipv6: bool = False):
    """Add a new iptables rule with optional source, destination, and logging."""
    cmd = ["sudo", "ip6tables" if ipv6 else "iptables", "-A", chain, "-p", protocol, "--dport", port, "-j", action]
    if source:
        cmd.extend(["-s", source])
    if dest:
        cmd.extend(["-d", dest])
    if log:
        cmd.extend(["-j", "LOG", "--log-prefix", "'Netfilter:'"])
    return run_command(cmd)

def delete_rule(chain: str, protocol: str, port: str, action: str, source: str = None, dest: str = None, ipv6: bool = False):
    """Delete an iptables rule with optional source and destination."""
    cmd = ["sudo", "ip6tables" if ipv6 else "iptables", "-D", chain, "-p", protocol, "--dport", port, "-j", action]
    if source:
        cmd.extend(["-s", source])
    if dest:
        cmd.extend(["-d", dest])
    return run_command(cmd)

def save_rules():
    """Save current iptables rules for persistence."""
    return run_command(["sudo", "iptables-save", "-c", ">", "/etc/iptables/rules.v4"])

def load_rules():
    """Reload saved iptables rules."""
    return run_command(["sudo", "iptables-restore", "<", "/etc/iptables/rules.v4"])

def main():
    """Main function to handle CLI arguments."""
    parser = argparse.ArgumentParser(description="Enhanced CLI for Linux Netfilter (iptables) management.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # List rules
    list_parser = subparsers.add_parser("list", help="List iptables rules")
    list_parser.add_argument("--ipv6", action="store_true", help="List IPv6 rules")

    # Add rule
    add_parser = subparsers.add_parser("add", help="Add an iptables rule")
    add_parser.add_argument("chain", help="Chain (e.g., INPUT, OUTPUT, FORWARD)")
    add_parser.add_argument("protocol", help="Protocol (e.g., tcp, udp)")
    add_parser.add_argument("port", help="Port number")
    add_parser.add_argument("action", help="Action (e.g., ACCEPT, DROP)")
    add_parser.add_argument("--source", help="Source IP address")
    add_parser.add_argument("--dest", help="Destination IP address")
    add_parser.add_argument("--log", action="store_true", help="Enable logging for this rule")
    add_parser.add_argument("--ipv6", action="store_true", help="Apply to IPv6")

    # Delete rule
    del_parser = subparsers.add_parser("delete", help="Delete an iptables rule")
    del_parser.add_argument("chain", help="Chain (e.g., INPUT, OUTPUT, FORWARD)")
    del_parser.add_argument("protocol", help="Protocol (e.g., tcp, udp)")
    del_parser.add_argument("port", help="Port number")
    del_parser.add_argument("action", help="Action (e.g., ACCEPT, DROP)")
    del_parser.add_argument("--source", help="Source IP address")
    del_parser.add_argument("--dest", help="Destination IP address")
    del_parser.add_argument("--ipv6", action="store_true", help="Apply to IPv6")

    # Save and load rules
    subparsers.add_parser("save", help="Save current iptables rules for persistence")
    subparsers.add_parser("load", help="Load saved iptables rules")

    args = parser.parse_args()

    if args.command == "list":
        print(list_rules(args.ipv6))
    elif args.command == "add":
        print(add_rule(args.chain, args.protocol, args.port, args.action, args.source, args.dest, args.log, args.ipv6))
    elif args.command == "delete":
        print(delete_rule(args.chain, args.protocol, args.port, args.action, args.source, args.dest, args.ipv6))
    elif args.command == "save":
        print(save_rules())
    elif args.command == "load":
        print(load_rules())

if __name__ == "__main__":
    main()
# In this version, we have added support for IPv6 rules by using the ip6tables command instead of iptables.
# The add and delete rule functions now include an ipv6 parameter to specify whether the rule should be applied to IPv6 traffic.
# The list_rules function also supports listing IPv6 rules by passing the --ipv6 flag to the list command.