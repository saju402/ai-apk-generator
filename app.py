import os
import subprocess

ANDROID_HOME = os.getenv("ANDROID_HOME")
BUILD_DIR = "build"
JAVA_FILE = f"{BUILD_DIR}/MainActivity.java"
APK_NAME = "MyApp.apk"
PACKAGE_NAME = "com.example.myapp"

os.makedirs(BUILD_DIR, exist_ok=True)

# 1. Java source generate
java_code = f"""
package {PACKAGE_NAME};

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {{
    @Override
    protected void onCreate(Bundle savedInstanceState) {{
        super.onCreate(savedInstanceState);
        TextView tv = new TextView(this);
        tv.setText("Hello from no-Gradle build!");
        setContentView(tv);
    }}
}}
"""
with open(JAVA_FILE, "w") as f:
    f.write(java_code)

# 2. Compile Java with android.jar
android_jar = f"{ANDROID_HOME}/platforms/android-30/android.jar"
subprocess.run([
    "javac", "-source", "1.8", "-target", "1.8",
    "-classpath", android_jar,
    "-d", BUILD_DIR,
    JAVA_FILE
], check=True)

# 3. Convert to DEX
subprocess.run([
    f"{ANDROID_HOME}/build-tools/30.0.3/d8",
    "--output", BUILD_DIR,
    f"{BUILD_DIR}/MainActivity.class"
], check=True)

# 4. Package APK
subprocess.run([
    f"{ANDROID_HOME}/build-tools/30.0.3/aapt", "package", "-f",
    "-M", "AndroidManifest.xml",
    "-I", android_jar,
    "-S", "res",
    "-A", "assets",
    "-F", f"{APK_NAME}.unsigned",
    BUILD_DIR
], check=True)

# 5. Sign APK
subprocess.run([
    f"{ANDROID_HOME}/build-tools/30.0.3/apksigner", "sign",
    "--ks", "debug.keystore",
    "--ks-pass", "pass:android",
    "--key-pass", "pass:android",
    "--ks-key-alias", "androiddebugkey",
    f"{APK_NAME}.unsigned"
], check=True)

print("✅ APK Build Complete:", APK_NAME)
