#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SkyEmie_' 💜 https://github.com/SkyEmie
programminghoch10 https://github.com/programminghoch10
"""

import time
#from flashbootlib import test
import os
import subprocess
import math

staticimei = 0          #enter your imei here if you dont want to be asked every start

def bruteforceBootloader(increment):

#    algoOEMcode = 0000000000000000
    algoOEMcode     = 1000000000000000  #base to start bruteforce from
    autoreboot      = False             #set this to True if you need to prevent the automatic reboot to system by the bootloader after x failed attempts, code will automatically set this to true if it detects a reboot by the bootloader
    autorebootcount = 4                 #reboot every x attemps if autoreboot is True, set this one below the automatic reboot by the bootloader
    savecount       = 200               #save progress every 200 attempts, do not set too low to prevent storage wearout
    unknownfail     = True              #fail if output is unknown, only switch to False if you have problems with this
    
    failmsg = "check password failed"   #used to check if code is wrong
    
    unlock=False
    n=0
    while (unlock == False):
        print("Bruteforce is running...\nCurrently testing code "+str(algoOEMcode).zfill(16)+"\nProgress: "+str(round((algoOEMcode/10000000000000000)*100, 2))+"%")
        output = subprocess.run("fastboot oem unlock " + str(algoOEMcode).zfill(16), shell=True, stderr=subprocess.PIPE).stderr.decode('utf-8')
        print(output)
        output = output.lower()
        n+=1

        if 'success' in output:
            bak = open("unlock_code.txt", "w")
            bak.write("Your saved bootloader code : "+str(algoOEMcode))
            bak.close()
            print("Your bruteforce result has been saved in \"unlock_code.txt\"")
            return(algoOEMcode)
        if 'reboot' in output:
            print("Target device has bruteforce protection!")
            print("Waiting for reboot and trying again...")
            os.system("adb wait-for-device")
            os.system("adb reboot bootloader")
            print("Device reboot requested, turning on reboot workaround.")
            autoreboot = True
        if failmsg in output:
            #print("Code " + str(algoOEMcode) + " is wrong, trying next one...")
            pass
        if 'success' not in output and 'reboot' not in output and failmsg not in output and unknownfail:
            # fail here to prevent continuing bruteforce on success or another error the script cant handle
            print("Could not parse output.")
            print("Please check the output above yourself.")
            print("If you want to disable this feature, switch variable unknownfail to False")
            exit()

        if (n%savecount==0):
            bak = open("unlock_code.txt", "w")
            bak.write("If you need to pick up where you left off,\nchange the algoOEMcode variable with #base comment to the following value :\n"+str(algoOEMcode))
            bak.close()
            print("Your bruteforce progress has been saved in \"unlock_code.txt\"")

        if (n%autorebootcount==0 and autoreboot):
            print("Rebooting to prevent bootloader from rebooting...")
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

print('\n\n           Unlock Bootloader script - By SkyEmie_\' and programminghoch10')
print('\n\n  (You must enable USB DEBUGGING and OEM UNLOCK in the developer options of the target device...)')
print('  !!! All data will be erased !!! \n')
#input(' Press enter to detect device..\n')

os.system('adb devices')

print("Please select \"Always allow from this computer\" in the adb dialog!")

checksum = 1
while (checksum != 0):
    if staticimei > 0: 
        imei = int(input('Type IMEI: '))
    if staticimei == 0:
        imei = staticimei
    checksum = luhn_checksum(imei)
    if (checksum != 0):
        print('IMEI incorrect!')
        if(staticimei > 0):
            exit()
increment = int(math.sqrt(imei)*1024)
input('Press enter to reboot your device...\n')
os.system('adb reboot bootloader')
#input('Press enter when your device is ready... (This may take time, depending on your phone)\n')

codeOEM = bruteforceBootloader(increment)

os.system('fastboot getvar unlocked')
#os.system('fastboot reboot')

print('\n\nDevice unlocked! OEM CODE: '+codeOEM+'\n')
exit()
