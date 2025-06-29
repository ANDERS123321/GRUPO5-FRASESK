from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

HISTORY_FILE = "quotes_history.txt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-quote', methods=['GET'])
def get_quote():
    response = requests.get('https://api.kanye.rest')
    data = response.json()
    quote = data.get("quote", "No quote found")


