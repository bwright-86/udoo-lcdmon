#!/bin/sh

mkdir /etc/systemd/scripts/
cp udoo-lcdmon/ /etc/systemd/scripts/ -r
cp systemd/udoo-lcdmon.service /etc/systemd/system/udoo-lcdmon.service
systemctl start udoo-lcdmon
systemctl enable udoo-lcdmon