from flask import Flask, request, jsonify
import time
import os  # ← नया import

app = Flask(__name__)

@app.route('/')
def home():
    return "AI APK Generator is Live!"

@app.route('/generate-apk', methods=['POST'])
def generate_apk():
    data = request.json
    app_name = data.get('app_name', 'MyApp')
    feature = data.get('feature', 'Basic Feature')

    # Java code generator function call
    generate_android_code(app_name, feature)

    time.sleep(3)

    return jsonify({
        "status": "success",
        "message": f"{app_name} generated successfully with {feature}",
        "apk_url": f"https://your-ai-server.com/apks/{app_name.lower().replace(' ', '_')}.apk"
    })

# ⬇️⬇️⬇️ यहाँ paste करो
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

# ⬇️⬇️⬇️ इसके नीचे कुछ नहीं
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
