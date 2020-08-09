#!/bin/bash
# this script can be run in the background when bruteforcing on a linux machine
# it will automatically reboot adb devices into the bootloader
# run it in the background like this: ./autoreboot.sh &
# use this only if your bootloader doesn't have the reboot protection,
#  or if it has reboot protection and you've set the autoreboot variable MANUALLY to True
#  else the bruteforce script could stop executing randomly
while true
do
adb wait-for-usb-device
adb reboot bootloader
done