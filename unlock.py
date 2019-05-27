#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sky' 💜 https://github.com/SkywalkerFR
https://fr.wikipedia.org/wiki/Formule_de_Luhn
"""

import time
#from flashbootlib import test
import os
import math

##########################################################################################################################

def tryUnlockBootloader(checksum):

    unlock      = False
    algoOEMcode = 1000000000000000 #base
    
    while(unlock == False):
        sdrout = str(os.system('fastboot oem unlock '+str(algoOEMcode)))
        sdrout = sdrout.split(' ')
        for i in sdrout:
            if i == 'success':
                return(algoOEMcode)

        algoOEMcode = algoIncrementChecksum(algoOEMcode, checksum)


def algoIncrementChecksum(genOEMcode, checksum):
    genOEMcode+=int(checksum+math.sqrt(imei)*1024)
    return(genOEMcode)

def luhn_checksum(imei):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(imei)
    oddDigits = digits[-1::-2]
    evenDigits = digits[-2::-2]
    checksum = 0
    checksum += sum(oddDigits)
    for i in evenDigits:
        checksum += sum(digits_of(i*2))
    return checksum % 10

##########################################################################################################################

print('\n\n           Unlock Bootloader script - By Sky\'')
print('\n\n  (Please enable USB DEBBUG and OEM UNLOCK if the device isn\'t appear..)')
print('  /!\ All data will be erased /!\\\n')
input(' Press any key to detect device..\n')

os.system('adb devices')

imei     = int(input('Type IMEI digit :'))
checksum = luhn_checksum(imei)
input('Press any key to reboot your device..\n')
os.system('adb reboot bootloader')
input('Press any key when your device is ready.. (This may take time, depending on your cpu/serial port)\n')

codeOEM = tryUnlockBootloader(checksum)

os.system('fastboot getvar unlocked')
os.system('fastboot reboot')

print('\n\nDevice unlock ! OEM CODE : '+codeOEM)
print('(Keep it safe)\n')
input('Press any key to exit..\n')
exit()
