# poke_captive_portal
cli registration of e-mail address with telia captive portal

## Installation
```
sudo cp -r poke_captive_portal /opt/
sudo cp /opt/poke_captive_portal/poke-telia.* /etc/systemd/system/
sudo cp /opt/poke_captive_portal/poke.conf /root/.config/
sudo systemctl enable --now poke-telia.timer
```

Ensure to adjust `~/.config/poke.conf` to your system.
