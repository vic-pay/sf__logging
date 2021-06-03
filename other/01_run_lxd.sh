#!/bin/bash
ansible-playbook \
    -i ../inventory.yml \
    -t "lxd" \
    ../playbook.yml