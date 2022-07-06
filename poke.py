#!/usr/local/bin/python3
#https://redirect.teliawifi.telia.com/portal?mac=be:ef:be:ef:be:ef
import psutil
import requests
psutil.net_if_addrs()
network_interface='iw0'
mac_address=list(psutil.net_if_addrs()[network_interface][2])[1]
print(f"if {network_interface} mac: {mac_address}")
response=requests.get(f'https://redirect.teliawifi.telia.com/portal?mac={mac_address}')
if response.status_code == 200:
  print(f'Telia recognizes mac ({mac_address})')
elif response.status_code == 404:
  print(f'Telia does not recognize mac ({mac_address})')
for varstring in response.url.split('?')[1].split('&'):
  namestr, value = varstring.split('=')
  exec("%s = '%s'" % (namestr, value))
print(f"session_token: {session_token}, traceparent: {traceparent}")
