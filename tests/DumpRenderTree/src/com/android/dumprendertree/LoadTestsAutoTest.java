/*
 * Copyright (C) 2008 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.android.dumprendertree;

import android.app.Instrumentation;
import android.content.Intent;

import android.util.Log;

import android.os.Bundle;
import android.os.Debug;
import android.os.Debug.MemoryInfo;
import android.test.ActivityInstrumentationTestCase2;

import com.android.dumprendertree.TestShellActivity;
import com.android.dumprendertree.TestShellCallback;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;

public class LoadTestsAutoTest extends ActivityInstrumentationTestCase2<TestShellActivity> {

    private final static String LOGTAG = "LoadTest";
    private final static String LOAD_TEST_RESULT = "/sdcard/load_test_result.txt";

    public LoadTestsAutoTest() {
        super("com.android.dumprendertree", TestShellActivity.class);
    }

    // This function writes the result of the layout test to
    // Am status so that it can be picked up from a script.
    public void passOrFailCallback(String file, boolean result) {
        Instrumentation inst = getInstrumentation();
        Bundle bundle = new Bundle();
        bundle.putBoolean(file, result);
        inst.sendStatus(0, bundle);
    }

    // Invokes running of layout tests
    // and waits till it has finished running.
    public void runTest() {
        LayoutTestsAutoRunner runner = (LayoutTestsAutoRunner) getInstrumentation();

        if (runner.mTestPath == null) {
            Log.e(LOGTAG, "No test specified");
            return;
        }

        TestShellActivity activity = (TestShellActivity) getActivity();

        // Run tests
        runTestAndWaitUntilDone(activity, runner.mTestPath, runner.mTimeoutInMillis);

        // TODO(fqian): let am instrumentation pass in the command line, currently
        // am instrument does not allow spaces in the command.
        dumpMemoryInfo();

        // Kill activity
        activity.finish();
    }

    private void dumpMemoryInfo() {
        try {
            Log.v(LOGTAG, "Dumping memory information.");

            FileOutputStream out = new FileOutputStream(LOAD_TEST_RESULT, true);
            PrintStream ps = new PrintStream(out);

            MemoryInfo mi = new MemoryInfo();
            Debug.getMemoryInfo(mi);

            //try to fake the dumpsys format
            //this will eventually be changed to XML
            String format = "%15s:%9d%9d%9d%9d";
            String pss =
              String.format(format, "(Pss)",
                  mi.nativePss, mi.dalvikPss, mi.otherPss,
                  mi.nativePss + mi.dalvikPss + mi.otherPss);
            String sd =
              String.format(format, "(shared dirty)",
                  mi.nativeSharedDirty, mi.dalvikSharedDirty, mi.otherSharedDirty,
                  mi.nativeSharedDirty + mi.dalvikSharedDirty + mi.otherSharedDirty);
            String pd =
              String.format(format, "(priv dirty)",
                  mi.nativePrivateDirty, mi.dalvikPrivateDirty, mi.otherPrivateDirty,
                  mi.nativePrivateDirty + mi.dalvikPrivateDirty + mi.otherPrivateDirty);

            ps.print("\n\n\n");
            ps.println("** MEMINFO in pid 0 [com.android.dumprendertree] **");
            ps.println("                   native   dalvik    other    total");
            ps.println("           size:    12060     5255      N/A    17315");
            ps.println("      allocated:    12060     5255      N/A    17315");
            ps.println("           free:    12060     5255      N/A    17315");
            ps.println(pss);
            ps.println(sd);
            ps.println(pd);
            ps.print("\n\n\n");
            ps.flush();
            ps.close();
            out.flush();
            out.close();
        } catch (IOException e) {
            Log.e(LOGTAG, e.getMessage());
        }
    }

    // A convenient method to be called by another activity.
    private void runTestAndWaitUntilDone(TestShellActivity activity, String url, int timeout) {
        activity.setCallback(new TestShellCallback() {
            public void finished() {
                synchronized (LoadTestsAutoTest.this) {
                    LoadTestsAutoTest.this.notifyAll();
                }
            }
        });

        Intent intent = new Intent(Intent.ACTION_VIEW);
        intent.setClass(activity, TestShellActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP);
        intent.putExtra(TestShellActivity.TEST_URL, url);
        intent.putExtra(TestShellActivity.TIMEOUT_IN_MILLIS, timeout);
        intent.putExtra(TestShellActivity.RESULT_FILE, LOAD_TEST_RESULT);
        activity.startActivity(intent);

        // Wait until done.
        synchronized (this) {
            try {
                this.wait();
            } catch (InterruptedException e) { }
        }
    }
}
