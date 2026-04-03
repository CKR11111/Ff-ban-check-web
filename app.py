from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    uid = request.form.get("uid")

    if not uid:
        return "❌ Enter UID"

    try:
        url = f"http://amin-team-api.vercel.app/check_banned?player_id={uid}"
        res = requests.get(url, timeout=10)

        if res.status_code == 200:
            return res.text
        else:
            return "❌ Server Error"

    except:
        return "❌ API Failed"

if __name__ == "__main__":
    app.run()