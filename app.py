from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder='formato')

HISTORY_FILE = "history.txt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-quote', methods=['GET'])
def get_quote():
    response = requests.get('https://api.kanye.rest')
    data = response.json()
    quote = data.get("quote", "No quote found")

# Creación del historial
    with open(HISTORY_FILE, 'a') as file:
        file.write(quote + '\n')

    return jsonify({"quote": quote})

@app.route('/history', methods=['GET'])
def get_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            quotes = file.readlines()
        quotes = [q.strip() for q in quotes if q.strip()]
        return jsonify({"history": quotes})
    except FileNotFoundError:
        return jsonify({"history": []})

if __name__ == '__main__':
    app.run(debug=True)

