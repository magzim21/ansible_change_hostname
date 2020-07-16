#!/usr/bin/env python2.7
import subprocess
import json
import sys, os

# TODO ADD EXCEPTIONS

try:
    if not os.path.isfile(sys.argv[1]):
        print "ERROR: File provided as argument does not exist"
        exit(1)
except IndexError:
    print "ERROR: json with hosts to rename was not provided.\n" \
          "Pass it as the first argument"
    exit(1)



# GETTING CURRENT HOSTNAME
get_hostname_cmd = "hostname"
process = subprocess.Popen(
    get_hostname_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
old_hostname, error = process.communicate()
if error:
    print "ERROR: Can not execute '" + get_hostname_cmd + "' command. Details:"
    print error
    exit(1)
print "old_hostname is " + old_hostname

# GETTING CURRENT IP
get_ip_cmd = "hostname -I"
process = subprocess.Popen(get_ip_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
host_ip, error = process.communicate()
if error:
    print "ERROR: Can not execute '" + get_ip_cmd + "' command. Details:"
    print error
    exit(1)
host_ip=host_ip.split()
print "host_ip is " + host_ip

# PARSING DATA FROM JSON
try:
    with open(sys.argv[1], 'r') as outfile:
        # json.dump(hostnames_list, outfile)
        hostnames_list = json.load(outfile)

except ValueError:
    print "ERROR: Provided json file is not valid"
    exit(1)

found = False
for ip, new_hostname in hostnames_list.items():
    if ip in host_ip:
        rename_host_cmd = "hostnamectl set-hostname " + new_hostname
        process = subprocess.Popen(
            rename_host_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, error = process.communicate()
        if error:
            print "ERROR: Can not execute '" + rename_host_cmd + "' command. Details:"
            print error
            exit(1)
        print "HOST RENAMED SUCCESSFULLY"
        found = True
        break

if not found:
    print "Hostname of current host was not found in a list.\n" \
    "So it was not renamed"

