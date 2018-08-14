#!/bin/bash

if [ $EUID != 0 ]; then
    apt update;
    apt install nginx php-fpm;
    ufw allow 'Nginx HTTP';
    ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//';
    exit $?
fi