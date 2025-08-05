from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI APK Generator is Live!"

@app.route('/generate-apk', methods=['POST'])
def generate_apk():
    data = request.json
    app_name = data.get('app_name', '')

    if app_name != 'ai-generator.apk':
        return jsonify({
            "status": "error",
            "message": "Invalid app name."
        }), 400

    feature = data.get('feature', 'Basic Feature')

    return jsonify({
        "status": "success",
        "message": f"APK generated for {app_name} with feature: {feature}",
        "apk_url": "https://dummy-download-link.com/app.apk"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
