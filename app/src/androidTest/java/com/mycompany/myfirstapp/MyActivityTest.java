package com.mycompany.myfirstapp;

import android.content.Intent;
import android.test.ActivityUnitTestCase;
import android.test.suitebuilder.annotation.MediumTest;
import android.widget.Button;

/**
 * Created by mattmcd on 01/08/15.
 */
public class MyActivityTest
        extends ActivityUnitTestCase<MyActivity> {

    private Intent mStartIntent;

    public MyActivityTest() {
        super(MyActivity.class);
    }


    @Override
    protected void setUp() throws Exception {
        super.setUp();
        // Start MyActivity
        mStartIntent = new Intent(getInstrumentation()
            .getTargetContext(), MyActivity.class);
        startActivity(mStartIntent, null, null);
    }

    @MediumTest
    public void testDisplayMessageIntentLaunched() {
        final Button sendButton =
                (Button) getActivity()
                .findViewById(R.id.button_send);
        sendButton.performClick();

        final Intent sendIntent = getStartedActivityIntent();
        assertNotNull("Intent was null", sendIntent);
    }
}
