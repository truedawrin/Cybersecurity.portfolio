#!/usr/bin/env bash
# A Bash-based network discovery utility that checks hosts in an authorized subnet.

# Allow passing the subnet prefix as an argument, or prompt if omitted
ip="$1"
if [[ -z "$ip" ]]; then
    read -rp "Enter the first three octets of an IP address (e.g., 192.168.1): " ip
fi

if [[ -z "$ip" ]]; then
    echo "Error: No IP prefix entered."
    echo "Usage: ./ipsweep.sh <first-three-octets>"
    exit 1
fi

# Clear previous logs before starting a new scan
: > ip-logs.txt

echo "Scanning $ip.1 to $ip.254..."

for host in {1..254}; do
    ping -c 1 -W 1 "$ip.$host" | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" | tee -a ip-logs.txt &
done

# Wait for all background ping jobs to finish before printing completion
wait

echo "-- Scan completed --"
echo "-- All logs have been saved to ip-logs.txt --"
