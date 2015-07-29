# Acceptance test using monkeyrunner
# Run using: monkyrunner test_app.py

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connect to device that is running the test
# To check which devices are running: adb devices
# To start an emulator: emulator -avd <device_name>
#   e.g. emulator -avd my_nexus7_API_22
# Note that Android/Sdk/{platform-tools,tools} need to be on path
device = MonkeyRunner.waitForConnection()

# Install the application package to this device
device.installPackage('app/build/outputs/apk/app-debug.apk')

# Set package and activity to be started
package = 'com.mycompany.myfirstapp'
activity = '.MyActivity'
runComponent = package +'/' + activity

# Run the activity on the device
device.startActivity(component=runComponent)


