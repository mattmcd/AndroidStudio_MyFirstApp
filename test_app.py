# Acceptance test using Android Client View
# Run using: python test_app.py
import os
import sys
import time
import subprocess
try:
    ANDROID_VIEW_CLIENT_HOME = os.environ['ANDROID_VIEW_CLIENT_HOME']
except:
    print 'VC Home not set'
    sys.exit(1)

sys.path.append(ANDROID_VIEW_CLIENT_HOME)

from com.dtmilano.android.viewclient import ViewClient

# Connect to device that is running the test
# To check which devices are running: adb devices
# To start an emulator: emulator -avd <device_name>
#   e.g. emulator -avd my_nexus7_API_22
# Note that Android/Sdk/{platform-tools,tools} need to be on path
device, serialno = ViewClient.connectToDeviceOrExit(serialno='emulator-5554')

# Install the application package to this device
with open(os.devnull, 'w') as devnull:
    subprocess.call(['adb', 'install',
    'app/build/outputs/apk/app-debug.apk'], stdout=devnull, stderr=devnull)


try:
    # Set package and activity to be started
    package = 'com.mycompany.myfirstapp'
    activity = '.MyActivity'
    runComponent = package +'/' + activity

    # Run the activity on the device
    device.startActivity(component=runComponent)

    # Pause
    time.sleep(2)
    activityName = device.getTopActivityName()

    vc = ViewClient(device, serialno)
    vc.dump()

    editMsg = vc.findViewByIdOrRaise( package + ':' + 'id/edit_message')
    editMsg.touch()
    editMsg.type('Hello world!')
    
    # Pause
    time.sleep(1)

    buttonSend = vc.findViewByIdOrRaise( package + ':' + 'id/button_send')
    buttonSend.touch();

    # Pause
    time.sleep(2)
    if not (device.getTopActivityName() == activityName) :
        # Activity crashed
        print 'Crashed!'

finally:
    # Uninstall 
    with open(os.devnull, 'w') as devnull:
        subprocess.call(['adb', 'uninstall', package], stdout=devnull,
        stderr=devnull);
