from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Termux वा Cloud मा चलाउनको लागि host='0.0.0.0' राखिएको छ
    app.run(debug=True, host='0.0.0.0', port=5000)
