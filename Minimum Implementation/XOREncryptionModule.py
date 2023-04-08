from __future__ import annotations
from typing import List
import string

# Todo: 1) Create a heavily simplified version of this module 
#       2) This implementation should have a 'problem' that is resolved
#           by the 'Improved Implementation'

# Each AppModule needs to have:
#   title: display name of the module
#   order: ordering priority; lower numbers will be displayed higher up

# Todo for XOR Cipher: 1) Make a CLI copy of this in 'Improved Implementation' that 'teaches' bitwise operators
 #       2) Write a simplified CLI version of this in 'Minimum Implementation' that illustrates the use of bitwise operators

# 0 for encode, 1 for decode
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

    for char in plain_text:
        cipher_text.append('0' if char == key[key_idx] else '1')
        key_idx = (key_idx+1)%len(key)

    print("Result:", end='')
    print(''.join(cipher_text))

if __name__ == "__main__":
    cipher("101010","111111")
    cipher("010101", "111111")


