from __future__ import annotations
from typing import List
import string

# This function takes in an inputText string and a key string, and performs a basic XOR cipher.
# The function prints the resulting ciphered text to the console.
# The function also performs input validation to ensure that the key and input are binary strings.

def cipher(inputText:str, key:str):
    # Input Validation
    if not len(key) > 0:
        print("Error. Please provide a key.")
        return
    for char in set(key).union(set(inputText)):
        if char not in ['0','1']:
            print("Error. In binary mode, the key and input must be binary.")
            return

    # The Validated Parameters
    key:List[str] = list(key)

    # Ciphering...
    plain_text = inputText
    cipher_text = []
    key_idx = 0

    # For each character in the inputText string, XOR it with the corresponding character in the key string.
    # Append the result to the cipher_text list.
    # The resulting ciphered text is a binary string.
    for char in plain_text:
        cipher_text.append('0' if char == key[key_idx] else '1')
        key_idx = (key_idx+1)%len(key)

# Print the resulting ciphered text to the console.
    print("Result:", end='')
    print(''.join(cipher_text))

# This code runs the cipher function with two different input strings.
# The output of each function call is printed to the console.
if __name__ == "__main__":
    cipher("101010","111111")
    cipher("010101", "111111")


