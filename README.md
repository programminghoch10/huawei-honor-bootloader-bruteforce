## Huawei-honor-unlock-bootloader (Python 3)

## Summary

After closing the official EMUI website, which allowed you to retrieve the code to unlock the bootloader of Huawei/Honor phones, here is a python script to retrieve it by yourself.

It uses a bruteforce method, based on the Luhn algorithm and the iMEI identifier used by the manufacturer to generate the unlocking code.

I've only had the opportunity to test it on European versions only.

## Instructions

### Connecting a device in ADB mode

1. Enable developer options in Android.

    * Go to Settings > System > About device and tap ‘Build number’ seven times to enable developer options.

2. Enable USB debugging in Android.

    * Android One: Go to Settings > System > Developer options and enable USB debugging.

3. Connect your device to the computer and launch the script. The device is going to ask for authorisation, which you'll have to allow.

4. Wait for the application to detect your device. The device info should appear.

## FAQ & Troubleshooting  

**The application doesn't work. Is there anything I should have installed?**  

Yes, it was developed in python so it needs it to run, version 3. You can install the latest version from [here](https://www.python.org/downloads/).

**The app on Windows doesn't detect my device even though it's connected and USB debugging is enabled. What could be the issue?**  

Windows most likely doesn't recognise your device in ADB mode. Install the universal ADB drivers from [here](http://dl.adbdriver.com/upload/adbdriver.zip), reboot your PC and try again.

**My phone reboot every 5 failed attempts**  
Sorry.. I've seen this in a few people and I have no idea. Its look like an additional protection. It happens on some models, having the same version, identical.
