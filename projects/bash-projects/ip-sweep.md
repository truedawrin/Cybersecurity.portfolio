# Bash IP Sweep

# Overview
**IP sweep or ICMP sweep** is a reconnaissance technique used to discover which IP addresses on a network are active/alive.


# Script
```
!/usr/bin/env bash

echo "enter an ip address to scan its subnet:"
read ip

if [ "$ip" == "" ]
                then
                echo "No ip entered"
                echo "Syntax: ./ipsweep.sh (ip address)"
else
     for Host in `seq 1 254`; do
     ping -c 1 $ip.$Host | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
     ping -c 1 $ip.$Host | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & >> ip-logs.txt
done
 echo " --Scan completed--"
 echo " --all logs has been sent to the ip-logs.txt file-- "
fi




```

# Showcase

[screenshot]([projects/bash-projects/images/image.png)](https://github.com/truedawrin/Cybersecurity.portfolio/blob/main/projects/bash-projects/images/image.png)
