import encrypt
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from joblib import load
from collections import Counter
import re
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
    model = load('new_model.joblib')
    feature = np.array([extact_feature(ciphertext)])
    key = model.predict(feature)[0]
    return encrypt_caesar(ciphertext, -key), key
    # key = model.predict(ciphertext)

def parse_input(req: str) ->str:
    cleaned_string = req.lower()
    cleaned_string = re.sub(r'[0-9\s,.!@#\$%\^\&*\)\(+=_-]', '', cleaned_string)
    print('cleaned string:\t',cleaned_string)
    return cleaned_string


@app.route('/caesar', methods=['POST'])
@cross_origin()
def caesar():
   req = request.get_json()
   req['cipher'] = parse_input(req['cipher'])
   
   result, key = decrypt_caesar(req['cipher'])
   response_data = {}
   response_data['plaintext'] = result
   response_data['key'] = key
   response_data['cipher_frequency'] = extact_feature(req['cipher'])
   response_data['plain_frequency'] = extact_feature(result)
   return response_data

@app.route('/encrypt', methods=['POST'])
@cross_origin
def encrypt():
    req = request.get_json()
    if not req['plaintext'] or not req['shift']:
        return jsonify({"error":
                        "input plaintext atau shift tidak boleh kosong"
                        }), 400 
    return encrypt_caesar(str(req['plaintext']), int(req["shift"]))

if __name__ == '__main__':
    app.run(debug=True, port=5000)


