import pandas as pd
import os

os.chdir(path='backend')
dataset = pd.read_csv('word.csv')

shifts = range(26)

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        else:
            result += char
    return result

plain = []
key = []
encrypted = []

for text in dataset['word']:
    for shift in shifts:
        key.append(shift)
        plain.append(text)
        enc = caesar_cipher_encrypt(text, shift)
        encrypted.append(enc)

df = pd.DataFrame({'plaintext':plain, 'cipher':encrypted, 'key':key})
df.to_excel(excel_writer='ouput.xlsx')