from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
from joblib import load
from collections import Counter
import numpy as np

# app config
app = Flask(__name__)
cors = CORS(app=app)
app.config['CORS_HEADERS'] = ['Accept', 'Content-Type']
app.config['CORS_Origin'] = '*'
app.config['CORS_Method'] = ['POST', 'OPTIONS', 'GET']


def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        else:
            result += char
    return result

def extact_feature(ciphertext):
     # a => 3, e => 5
    frequency = Counter(ciphertext)

    total = sum(frequency.values())
    features = [frequency.get(chr(i), 0) / total for i in range(ord('a'), ord('z') + 1)]
    # [0.2, 0.4]
    return features

def decrypt_caesar(ciphertext):
    model = load('predict_shift.joblib')
    feature = np.array([extact_feature(ciphertext)])
    key = model.predict(feature)[0]
    return encrypt_caesar(ciphertext, -key)
    # key = model.predict(ciphertext)


@app.route('/caesar', methods=['POST'])
@cross_origin()
def caesar():
   req = request.get_json()
   response_data = {}
   response_data['plaintext'] = decrypt_caesar(req['cipher'])
   response_data['frequency'] = extact_feature(req['cipher'])
   return response_data
   

if __name__ == '__main__':
    app.run(debug=True, port=5000)


