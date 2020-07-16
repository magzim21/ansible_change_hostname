# ANSIBLE batch rename hostnames

#### It works with **systemd**, but can easily be adopted for init systems.

1. Put desired information into hostnames.json
3. Comment out  whole 'ZABBIX SECTION' in pl-rename.yml if zabbix is not installed.
2. Run 
`ansible-playbook pl-rename.yml --extra-vars="hosts_group=<name of hostgroup from your 'hosts' file>"`
4. Enjoy :100: 
