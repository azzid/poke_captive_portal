# poke_captive_portal
cli registration of e-mail address with telia captive portal

## Installation
```
sudo cp -r poke_captive_portal /opt/
sudo cp /opt/poke_captive_portal/poke-telia.* /etc/systemd/system/
sudo cp /opt/poke_captive_portal/poke.conf /root/.config/
sudo systemctl enable --now poke-telia.timer
sudo cp /opt/poke_captive_portal/poke.sh /etc/NetworkManager/dispatcher.d/
```

Ensure to adjust `~/.config/poke.conf` and `/etc/systemd/system/poke-telia.service` to your system.
