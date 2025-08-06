from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "AI APK Generator is Live!"

@app.route('/generate-apk', methods=['POST'])
def generate_apk():
    data = request.json
    app_name = data.get('app_name', 'MyApp')
    feature = data.get('feature', 'Basic Feature')

    time.sleep(3)

    return jsonify({
        "status": "success",
        "message": f"{app_name} generated successfully with {feature}",
        "apk_url": f"https://your-ai-server.com/apks/{app_name.lower().replace(' ', '_')}.apk"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
