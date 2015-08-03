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

    def testEnterTextAndSendMessage(self):
        # Run the activity on the device
        self.startMyActivity()
        self.enterHelloWorldInEditBox()
        self.pressSendButton()
        # Check that we respond to input and user actions
        self.checkThatCurrentActivityIs('.DisplayMessageActivity')
        self.checkThatMessageIsDisplayed(
            'id/text_message', self.TEST_MESSAGE)

    def startMyActivity(self):
        runComponent = self.package +'/' + self.activity
        self.device.startActivity(component=runComponent)
        # Pause
        time.sleep(1)
        activityName = self.device.getTopActivityName()
        self.vc = ViewClient(self.device, self.serialno)
        self.vc.dump()

    def enterHelloWorldInEditBox(self):
        editMsg = self.getViewById('id/edit_message')
        editMsg.touch()
        editMsg.type(self.TEST_MESSAGE)
        
    def pressSendButton(self):
        buttonSend = self.getViewById('id/button_send')
        buttonSend.touch();
        time.sleep(1)
        
    def checkThatCurrentActivityIs(self, name):
        assert( self.device.getTopActivityName() == 
            (self.package + '/' + name) )
        
    def checkThatMessageIsDisplayed(self, view_id, msg):
        # Update view client
        self.vc.dump()
        textDisplay = self.getViewById(view_id).getText();
        assert( textDisplay == msg )

    def getViewById(self, view_id):
        view_instance = self.vc.findViewByIdOrRaise( 
            self.package + ':' + view_id )
        return view_instance
        
    def __init__(self):
        self.device = None
        self.serialno = None
        self.vc = None
        # Set package and activity to be started
        self.package = 'com.mycompany.myfirstapp'
        self.activity = '.MyActivity'
        self.TEST_MESSAGE = 'This is a test message'

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
    
    def tearDown(self):
        # Uninstall 
        with open(os.devnull, 'w') as devnull:
            subprocess.call(
            ['adb', 'uninstall', self.package], stdout=devnull,
            stderr=devnull);
