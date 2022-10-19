#!/usr/bin/env python3
import os       # use external tool to query which ssid is currently connected
import psutil   # access network interface information
import requests # ability to do web requests
import sys      # use sys.exit() rather than exit()

# Verify that we're connected to the expected ssid
expected_ssid='Telia WiFi'
current_ssid=os.popen("iwgetid").read().split('"')[1]
if not current_ssid == expected_ssid:
  print(f'not connected to {expected_ssid}', file=sys.stderr)
  sys.exit(1)

# Read which e-mail to supply from file
try:
  with open(os.path.expanduser('~/.config/poke.conf'), 'r') as file:
    for line in file:
      if 'email' in line:
        email=line.strip().split('=')[1].strip("\"\'")
except FileNotFoundError:
  #print(f"setting default e-mail")
  email='user@email.com'
except Exception as e:
  print(f"unexpected exception: {e}")
  email='user@email.com'

# Define e-mail to register with
post_json={ "email": email }

#network_interface='iw0' # let iwgetid figure this out instead
network_interface=os.popen("iwgetid").read().split('"')[0].split()[0]
mac_address=list(psutil.net_if_addrs()[network_interface][2])[1]

# Get session_token for mac address
#  first logout old session
logout_response=requests.get('http://login.homerun.telia.com/sd/logout')
#  then begin the new login attempt
response=requests.get(f'https://redirect.teliawifi.telia.com/portal?mac={mac_address}')
#  print a message if ok
if response.status_code == 200:
  print(f'Telia recognizes mac ({mac_address})')
#  quit if not ok
elif response.status_code == 404:
  print(f'Telia does not recognize mac ({mac_address}).')
  sys.exit(2)
# parse response url for necessary token data
for varstring in response.url.split('?')[1].split('&'):
  namestr, value = varstring.split('=')
  exec("%s = '%s'" % (namestr, value))

# Register e-mail for session
post_response=requests.post(f'https://cp.teliawifi.telia.com/TW-Reg/api/telia/v1/email_registration/{session_token}', json = post_json)

# Print result
if post_response.status_code == 204:
  print(f"Successful post of e-mail address [{email}]!")
else:
  print(f"unknown error, post http status code: '{post_response.status_code}")
