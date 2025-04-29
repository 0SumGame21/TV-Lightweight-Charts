from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('gainers.html')

@app.route("/static/gainers_data.json")
def gainers_data():
    return send_from_directory('static', 'gainers_data.json')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
