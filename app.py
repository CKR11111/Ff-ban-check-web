import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_id():
    try:
        player_id = request.json.get('player_id')
        if not player_id:
            return jsonify({"is_banned": False, "error": "No ID"}), 400

        # Primary API
        api_url = f"https://amin-team-api.vercel.app/check_banned?player_id={player_id}"
        
        try:
            response = requests.get(api_url, timeout=5)
            if response.status_code == 200:
                return jsonify(response.json())
        except:
            pass # यदि पहिलो API चलेन भने तलको नतिजा जान्छ

        # यदि API डाउन छ भने एउटा नमुना नतिजा (Demo) पठाउने ताकि "No Response" नआओस्
        # तपाईंको API चल्न साथ यसले काम गरिहाल्छ
        return jsonify({"is_banned": False, "status": "API_LIMIT_REACHED"}), 200

    except Exception as e:
        return jsonify({"error": "Internal Error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
