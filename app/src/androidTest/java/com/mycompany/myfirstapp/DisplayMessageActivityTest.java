package com.mycompany.myfirstapp;

import android.content.Intent;
import android.test.ActivityUnitTestCase;
import android.widget.TextView;

/**
 * Created by mattmcd on 01/08/15.
 */
public class DisplayMessageActivityTest
    extends ActivityUnitTestCase<DisplayMessageActivity> {

    private final String mTestMessage = "This is a test";
    private Intent mDisplayIntent;

    public DisplayMessageActivityTest(){
        super(DisplayMessageActivity.class);
    }

    @Override
    public void setUp() throws Exception{
        // Create the activity with intent containing message
        super.setUp();
        mDisplayIntent = new Intent(getInstrumentation()
                .getTargetContext(), DisplayMessageActivity.class);
        mDisplayIntent.putExtra(MyActivity.EXTRA_MESSAGE, mTestMessage);
        startActivity(mDisplayIntent, null, null);
    }

    public void testMessageIsDisplayed(){
        assertNotNull("Intent was null", mDisplayIntent);
        // Get the text display field
        TextView textDisplay = (TextView) getActivity().findViewById(R.id.text_message);
        assertEquals(textDisplay.getText().toString(), mTestMessage);
    }
}
