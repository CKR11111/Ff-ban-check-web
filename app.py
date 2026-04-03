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
            return jsonify({"error": "UID required"}), 400

        # Tapaiँko working API URL
        api_url = f"https://amin-team-api.vercel.app/check_banned?player_id={player_id}"
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": "API Error"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
