#!/usr/local/bin/python3
#https://redirect.teliawifi.telia.com/portal?mac=be:ef:be:ef:be:ef
import psutil
psutil.net_if_addrs()
network_interface='iw0'
mac_address=list(psutil.net_if_addrs()[network_interface][2])[1]
print(f"if {network_interface} mac: {mac_address}")
