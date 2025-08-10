import os
import time

def generate_android_code(app_name, feature):
    folder_name = app_name.lower().replace(" ", "_")
    os.makedirs(folder_name, exist_ok=True)

    java_code = f"""
package com.example.{folder_name};

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {{
    @Override
    protected void onCreate(Bundle savedInstanceState) {{
        super.onCreate(savedInstanceState);
        TextView tv = new TextView(this);
        tv.setText("{app_name} - Feature: {feature}");
        setContentView(tv);
    }}
}}
"""
    java_path = f"{folder_name}/MainActivity.java"
    with open(java_path, "w") as f:
        f.write(java_code)

if __name__ == "__main__":
    app_name = "MyApp"
    feature = "Basic Feature"
    generate_android_code(app_name, feature)
    time.sleep(3)
    print(f"✅ {app_name} generated successfully with {feature}")
