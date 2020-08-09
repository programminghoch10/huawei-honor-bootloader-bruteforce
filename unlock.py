#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SkyEmie_' 💜 https://github.com/SkyEmie
programminghoch10 https://github.com/programminghoch10
"""

import time
#from flashbootlib import test
import os
import math

def bruteforceBootloader(increment):

#    algoOEMcode = 0000000000000000
    algoOEMcode     = 1000000000000000  #base to start bruteforce from
    algoOEMcode     = 1853054182318208  #entire brute force progress
    autoreboot      = False             #set this to True if you need to prevent the automatic reboot to system by the bootloader after x failed attempts, code will automatically set this to true if it detects a reboot by the bootloader
    autorebootcount = 4                 #reboot every x attemps if autoreboot is True, set this one below the automatic reboot by the bootloader
    savecount       = 200               #save progress every 200 attempts, do not set too low to prevent storage wearout
    
    unlock=False
    n=0
    while (unlock == False):
        print("echo Bruteforce is running...\nCurrently testing code "+str(algoOEMcode).zfill(16)+"\nProgress: "+str(round((algoOEMcode/10000000000000000)*100, 2))+"%")
        sdrout = str(os.system('fastboot oem unlock '+ str(algoOEMcode).zfill(16)))
        sdrout = sdrout.split(' ')
        n+=1

        for i in sdrout:
            if i == 'success':
                bak = open("unlock_code.txt", "w")
                bak.write("Your saved bootloader code : "+str(algoOEMcode))
                bak.close()
                print("Your bruteforce result has been saved in \"unlock_code.txt\"")
                return(algoOEMcode)
            if i == 'reboot':
                os.system("adb wait-for-device")
                os.system("adb reboot bootloader")
                autoreboot = True

        if (n%savecount==0):
            bak = open("unlock_code.txt", "w")
            bak.write("If you need to pick up where you left off,\nchange the algoOEMcode variable with #base comment to the following value :\n"+str(algoOEMcode))
            bak.close()
            print("Your bruteforce progress has been saved in \"unlock_code.txt\"")

        if (n%autorebootcount==0 and autoreboot):
            os.system('fastboot reboot bootloader')

        algoOEMcode += increment

        if (algoOEMcode > 10000000000000000):
            print("OEM Code not found!\n")
            os.system("fastboot reboot")
            exit()

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


# Bruteforce setup:

print('\n\n           Unlock Bootloader script - By SkyEmie_\'')
print('\n\n  (You must enable USB DEBUGGING and OEM UNLOCK in the developer options of the target device...)')
print('  !!! All data will be erased !!! \n')
#input(' Press enter to detect device..\n')

os.system('adb devices')

print("Please select \"Always allow from this computer\" in the adb dialog!")

checksum = 1
while (checksum != 0):
    imei = int(input('Type IMEI: '))
    checksum = luhn_checksum(imei)
    if (checksum != 0):
        print('IMEI incorrect!')
increment = int(math.sqrt(imei)*1024)
input('Press enter to reboot your device...\n')
os.system('adb reboot bootloader')
#input('Press enter when your device is ready... (This may take time, depending on your phone)\n')

codeOEM = bruteforceBootloader(increment)

os.system('fastboot getvar unlocked')
#os.system('fastboot reboot')

print('\n\nDevice unlocked! OEM CODE: '+codeOEM+'\n')
exit()
