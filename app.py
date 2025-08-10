import os
import subprocess
import shutil

APP_NAME = "MyApp"
FEATURE = "Basic Feature"
PACKAGE = "com.example.myapp"

# Paths
TEMPLATE_DIR = "android-template/app"
BUILD_DIR = "build"
APK_OUTPUT_DIR = "output"
JAVA_FILE = os.path.join(BUILD_DIR, "MainActivity.java")

def prepare_folders():
    shutil.rmtree(BUILD_DIR, ignore_errors=True)
    shutil.rmtree(APK_OUTPUT_DIR, ignore_errors=True)
    os.makedirs(BUILD_DIR, exist_ok=True)
    os.makedirs(APK_OUTPUT_DIR, exist_ok=True)

def generate_java_code():
    java_code = f"""
package {PACKAGE};

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {{
    @Override
    protected void onCreate(Bundle savedInstanceState) {{
        super.onCreate(savedInstanceState);
        TextView tv = new TextView(this);
        tv.setText("{APP_NAME} - Feature: {FEATURE}");
        setContentView(tv);
    }}
}}
"""
    with open(JAVA_FILE, "w") as f:
        f.write(java_code)

def build_apk():
    # Compile Java to class
    subprocess.run([
        "javac", "-source", "1.8", "-target", "1.8",
        "-bootclasspath", "/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/rt.jar",
        "-classpath", TEMPLATE_DIR,
        "-d", BUILD_DIR,
        JAVA_FILE
    ], check=True)

    # Convert to DEX
    subprocess.run([
        "d8", "--output", BUILD_DIR, os.path.join(BUILD_DIR, "MainActivity.class")
    ], check=True)

    # Package APK
    apk_path = os.path.join(APK_OUTPUT_DIR, f"{APP_NAME}.apk")
    subprocess.run([
        "aapt", "package", "-f", "-M", os.path.join(TEMPLATE_DIR, "AndroidManifest.xml"),
        "-I", "/usr/lib/android-sdk/platforms/android-30/android.jar",
        "-F", apk_path,
        BUILD_DIR
    ], check=True)

    # Sign APK
    subprocess.run([
        "apksigner", "sign", "--ks", "debug.keystore",
        "--ks-pass", "pass:android", apk_path
    ], check=True)

    print(f"✅ APK Generated: {apk_path}")

if __name__ == "__main__":
    prepare_folders()
    generate_java_code()
    build_apk()
