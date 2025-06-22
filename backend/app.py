# === backend/app.py ===
from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

from preprocess import clean_text
import joblib
model = joblib.load('sms_spam_classifier.joblib')

app = Flask(__name__)
CORS(app)




@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    message = clean_text(data.get('message', ''))
    prediction = model.predict([message])[0]
    return jsonify({"classification": prediction})

if __name__ == '__main__':
    app.run(debug=True)