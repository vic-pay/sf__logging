#!/bin/bash
ansible-playbook \
    -i ../inventory.yml \
    -t "elk_repo,elk_server" \
    -l "sf-logging-server-2" \
    ../playbook.yml