#!/bin/bash
# this script can be run in the background when bruteforcing on a linux machine
# it will automatically reboot adb devices into the bootloader
# run it in the background like this: ./autoreboot.sh &
while true
do
adb wait-for-usb-device
adb reboot bootloader
done