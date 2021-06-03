#!/bin/bash
ansible-playbook \
    -i ../inventory.yml \
    -t "elk_repo,elk_agent,log_app,rsyslog_client" \
    -l "sf-logging-server-1" \
    ../playbook.yml