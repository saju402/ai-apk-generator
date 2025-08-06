from flask import Flask, request, jsonify
import os  # ये जरूरी है Render ke PORT के लिए

app = Flask(__name__)

@app.route('/')
def home():
    return "AI APK Generator is Live!"

@app.route('/generate-apk', methods=['POST'])
def generate_apk():
    data = request.json
    app_name = data.get('app_name', 'MyApp')
    feature = data.get('feature', 'Basic Feature')

    return jsonify({
        "status": "success",
        "message": f"APK generated for {app_name} with feature: {feature}",
        "apk_url": "https://dummy-download-link.com/app.apk"
    })
@app.route('/parse-prompt', methods=['POST'])
def parse_prompt():
    data = request.json
    prompt = data.get('prompt', '')

    parsed = {
        "app_name": "Violence AI Studio",
        "features": ["text-to-video", "voiceover", "text-to-image"]
    }

    return jsonify({
        "status": "success",
        "parsed_data": parsed
    })
if __name__ == '__main__':
    # Render par port fix nahi hota, isliye env se lena padta hai
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
