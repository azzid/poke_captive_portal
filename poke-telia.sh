#!/bin/bash
if [ "$1" = "<wifi interface>" ] && [ "$2" = "up" ]; then
  systemctl start poke-telia.service
fi
