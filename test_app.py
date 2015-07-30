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

class TestAppEndToEnd():

    def __init__(self):
        self.device = None
        self.serialno = None
        # Set package and activity to be started
        self.package = 'com.mycompany.myfirstapp'
        self.activity = '.MyActivity'
        self.runComponent = self.package +'/' + self.activity

    def setUp(self):
        # Connect to device that is running the test
        # To check which devices are running: adb devices
        # To start an emulator: emulator -avd <device_name>
        #   e.g. emulator -avd my_nexus7_API_22
        # Note that Android/Sdk/{platform-tools,tools} need to be on path
        self.device, self.serialno = ViewClient.connectToDeviceOrExit(
            serialno='emulator-5554')
        self.device.unlock()

        # Install the application package to this device
        with open(os.devnull, 'w') as devnull:
            subprocess.call(['adb', 'install',
            'app/build/outputs/apk/app-debug.apk'], 
            stdout=devnull, stderr=devnull)

    def testEnterTextAndSendMessage(self):

        # Run the activity on the device
        self.device.startActivity(component=self.runComponent)

        # Pause
        time.sleep(1)
        activityName = self.device.getTopActivityName()

        vc = ViewClient(self.device, self.serialno)
        vc.dump()

        editMsg = vc.findViewByIdOrRaise( 
            self.package + ':' + 'id/edit_message')
        editMsg.touch()
        editMsg.type('Hello world!')
        
        # Pause
        time.sleep(1)

        buttonSend = vc.findViewByIdOrRaise( 
            self.package + ':' + 'id/button_send')
        buttonSend.touch();

        # Pause
        time.sleep(1)
        assert(self.device.getTopActivityName() == activityName)

    def tearDown(self):
        # Uninstall 
        with open(os.devnull, 'w') as devnull:
            subprocess.call(
            ['adb', 'uninstall', self.package], stdout=devnull,
            stderr=devnull);
