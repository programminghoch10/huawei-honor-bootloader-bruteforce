#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sky'
"""

import time
#from flashbootlib import test
import os
import math


print('\n\n           Lock Bootloader script - By Sky\'')
print('\n\n  (Please enable USB DEBBUG and OEM UNLOCK if the device isn\'t appear..)')
print('  /!\ All data will be erased /!\\\n')
input(' Press any key to detect device..\n')


os.system('adb devices')

OEM = int(input('Type OEM code :'))
input('Press any key to reboot your device..\n')
os.system('adb reboot bootloader')
input('Press any key when your device is ready..\n')

os.system('fastboot oem relock '+OEM)

os.system('fastboot getvar unlocked')
os.system('fastboot reboot')

print('\n\nDevice lock !)
input('Press any key to exit..\n')
exit()
