# Netsimpler
**Netsimpler**
is a CLI-based user interface designed to simplify the management of Linux Netfilter (iptables and ip6tables) firewall rules.
This tool provides an intuitive CLI with enhanced functionality, including IPv6 support, rule persistence, detailed logging, and granular rule management.

**Features:**<br>
Manage both IPv4 and IPv6 firewall rules.<br>
Add and remove rules with fine-grained control (source/destination IPs, logging).<br>
Persist firewall rules to survive reboots.<br>
Logging support for monitoring traffic activity.<br>
Save current rules to a JSON file.<br>
Load rules from a saved file.<br>
Delete existing rules by specifying chain and rule number.<br>
Interactive CLI for ease of use.

**Installation:**<br>
***Clone the repository:***
``
git clone https://github.com/your-repo/netfilter.git
``<br>
***Go to Netsimpler repository dir:***
``
cd netfilter
``<br>
***Make the script executable:***
``chmod +x netsimpler.py``<br>
Ensure you have Python installed (Python 3.6+ required).<br>
Run the script with appropriate commands as described below.

**Usage:**<br>
***List Firewall Rules:***<br>
IPv4 Rules:
``
python netsimpler.py list
``<br>
IPv6 Rules:
``
python netsimpler.py list --ipv6
``<br>
***Add a Firewall Rule:***<br>
To add a rule, specify the chain, protocol, port, and action:
``
python netsimpler.py add INPUT tcp 80 ACCEPT
``<br>
***Additional Options:***<br>
Specify source IP: ``--source 192.168.1.1``<br>
Specify destination IP: ``--dest 10.0.0.1``<br>
Enable logging for the rule: ``--log``<br>
Apply to IPv6: ``--ipv6``<br>
Example:``python netsimpler.py add INPUT tcp 443 ACCEPT --log --source 192.168.1.100``<br>
***Delete a Firewall Rule:***<br>
To remove a rule, use the same parameters as when adding it:
``python netsimpler.py delete INPUT tcp 80 ACCEPT``<br>
Additional options (if the rule has these attributes):
``python netsimpler.py delete INPUT tcp 443 ACCEPT --source 192.168.1.100``<br>
***Save and Load Rules:***<br>
To make firewall rules persistent:<br>
Save current rules:
``python netsimpler.py save``<br>
Reload saved rules:
``python netsimpler.py load``<br>
***Permissions:***<br>
This script requires sudo privileges to modify firewall rules. If needed, run:
``sudo python netsimpler.py <command>``<br>

**Notes:**<br>
This tool is an alternative to ufw but provides more control for advanced users.
Use iptables-save and iptables-restore for manual rule backups if needed.
Always test firewall rules to ensure they don't block essential services.<br>
***Advantages Over UFW:***<br>
More Granular Rule Control – Advanced options while maintaining simplicity<br>
Interactive CLI – Guided step-by-step rule configuration<br>
Improved Logging & Monitoring – Enhanced debugging<br>
Configurable Rule Profiles – Easily switch between predefined rulesets<br>
Better Script Integration – Provides an API for automation<br>
JSON/YAML Rule Management – Structured and human-readable rule configurations<br>

**Contributing:**
Contributions are welcome! Please submit issues and pull requests to improve the tool.

**License:**
MIT License

