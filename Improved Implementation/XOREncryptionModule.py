from __future__ import annotations
from typing import List
import string

def cipher(inputText:str, key:str, isAscii: bool):
    # Input Validation
    if not len(key) > 0:
        print("Error. Please provide a key.")
        return
    if isAscii == False:
        for char in set(key).union(set(inputText)):
            if char not in ['0','1']:
                print("Error. In binary mode, the key and input must be binary.")
                return
    else: #if ascii is true
        for char in set(key).union(set(inputText)):
            if not ord(char) < 128:
                print("Error. In binary mode, the key and input must be binary.")
                return

    # The Validated Parameters
    key:List[str] = list(key)

    # Ciphering...
    plain_text = inputText
    cipher_text = []
    key_idx = 0

    for char in plain_text:
        if isAscii == True:
            #print(chr(ord(char)^ord(key[key_idx])))
            cipher_text.append(chr(ord(char)^ord(key[key_idx])))
        else:
            cipher_text.append('0' if char == key[key_idx] else '1')
        key_idx = (key_idx+1)%len(key)

    print("Result:", end='')
    print(''.join(cipher_text))

if __name__ == "__main__":
    cipher("101010", "111111", isAscii= False)
    cipher("010101", "111111", isAscii= False)

    