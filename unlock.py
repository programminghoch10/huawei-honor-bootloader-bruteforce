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
import random
import string

useletters = False      #set to True to include letters for random code generation
quickstart = False      #set to True to not need to confirm on script start

def bruteforceBootloader():

    autoreboot      = False             #set this to True if you need to prevent the automatic reboot to system by the bootloader after x failed attempts, code will automatically set this to true if it detects a reboot by the bootloader
    autorebootcount = 4                 #reboot every x attemps if autoreboot is True, set this one below the automatic reboot by the bootloader
    unknownfail     = True              #fail if output is unknown, only switch to False if you have problems with this
    
    failmsg = "check password failed"   #used to check if code is wrong
    
    unlock=False
    n=0
    algoOEMcode     = 0 
    while (unlock == False):
        
        if useletters:
            algoOEMcode = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
        else:
            algoOEMcode = str(random.randint(0,9999999999999999)).zfill(16)
                
        print("Bruteforce is running...\nCurrently testing code "+ algoOEMcode)
        output = subprocess.run("fastboot oem unlock " + algoOEMcode, shell=True, stderr=subprocess.PIPE).stderr.decode('utf-8')
        print(output)
        output = output.lower()
        n+=1

        if 'success' in output:
            bak = open("unlock_code.txt", "w")
            bak.write("Your saved bootloader code : "+algoOEMcode)
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
            #print("Code " + algoOEMcode + " is wrong, trying next one...")
            pass
        if 'success' not in output and 'reboot' not in output and failmsg not in output and unknownfail:
            # fail here to prevent continuing bruteforce on success or another error the script cant handle
            print("Could not parse output.")
            print("Please check the output above yourself.")
            print("If you want to disable this feature, switch variable unknownfail to False")
            exit()

        if (n%autorebootcount==0 and autoreboot):
            print("Rebooting to prevent bootloader from rebooting...")
            os.system('fastboot reboot bootloader')

# Bruteforce setup:

print('\n\n           Unlock Bootloader script - By SkyEmie_\' and programminghoch10')
print('\n\n  (You must enable USB DEBUGGING and OEM UNLOCK in the developer options of the target device...)')
print('  !!! All data will be erased !!! \n')
#input(' Press enter to detect device..\n')

os.system('adb devices')

print("Please select \"Always allow from this computer\" in the adb dialog!")

if quickstart==False:
    input('Press enter to reboot your device...\n')
os.system('adb reboot bootloader')
#input('Press enter when your device is ready... (This may take time, depending on your phone)\n')

codeOEM = bruteforceBootloader()

os.system('fastboot getvar unlocked')
#os.system('fastboot reboot')

print('\n\nDevice unlocked! OEM CODE: '+codeOEM+'\n')
exit()
