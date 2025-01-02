from collections import Counter
import re

# test case:
# 1. problem di program python
# 2. model underfitting atau overfitting
# 3. AI salah nerjemahin

def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        else:
            result += char
    return result

# plain1 = 
print("plaintext:" + encrypt_caesar)