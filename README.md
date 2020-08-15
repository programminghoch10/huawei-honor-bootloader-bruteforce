# huawei-honor-unlock-bootloader

## Summary

After closing the official EMUI website,
which allowed you to retrieve the code to unlock the bootloader of Huawei/Honor phones, 
here is a python script to test random codes.

This will most likely only work on European versions, 
because these only use numbers in the bootloader unlock code.

I've only had the opportunity to test it on European versions:
- Honor  5x 8x and 9x
- Honor  view 10 and 20
- Honor  10 lite
- Huawei p20 lite
- Huawei Y6 2019
- Huawei P20 Pro
- Huawei p30


## Instructions

1. Enable developer options in Android.
1. Enable USB debugging in Android.
1. Connect your device to the computer and launch the script.

    Windows:
    ```batch
    C:\WINDOWS\system32> python unlock.py
    ```
    Linux:
    ```shell
    $ python3 unlock.py
    ```
    The device is going to ask for authorisation, which you'll have to allow.  
    Please also check the checkbox "Always allow from this computer".
1. Wait for the application to detect your device. The device info should appear.
1. Start the bruteforce.  
    (this may take several ~~hours~~ thousand years) so ~~get a cup of coffee ☕ and go to sleep 💫~~ live your life and forget about this.
1. If the correct code is found, your phone will either be instantly unlocked or prompt you with an additional confirmation dialogue on the target device.  
    (all data will be erased on unlock!)


## FAQ & Troubleshooting

**- The application doesn't work. Is there anything I should have installed?**  
Yes, it was developed in python so it needs it to run, version 3. You can install the latest version from [here](https://www.python.org/downloads/) or by using Windows Store.

**- The app on Windows doesn't detect my device even though it's connected and USB debugging is enabled. What could be the issue?**  
Windows most likely doesn't recognise your device in ADB mode. Install the universal ADB drivers from [here](http://dl.adbdriver.com/upload/adbdriver.zip), reboot your PC and try again.

**- My phone reboots every 5 failed attempts**  
We are aware of this and have implemented an automatic intentional reboot after 4 attempts.  
You can manually enable this feature in the code.  
The script will also automatically detect this behaviour. For this to work reliably, please check the checkbox "Always allow from this computer" in the adb dialogue.

**- The script displays "command invalid"**  
Huawei has removed the unlock command in EMUI 10.  
Downgrade your software and try again.