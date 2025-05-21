# app.py
from flask import Flask, render_template, request, jsonify
from main import get_healthcare_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No input received'}), 400
    
    reply = get_healthcare_response(user_input)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True, port=5050)
