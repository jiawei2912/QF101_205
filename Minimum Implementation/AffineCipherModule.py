from __future__ import annotations
from typing import List
from PyQt5 import QtWidgets
from math import gcd
import string

# Todo: 1) Remove the use of the Class and the GUI
#       2) You can use functions
#       3) Simplify this into a standalone file

# Each AppModule needs to have:
#   title: display name of the module
#   order: ordering priority; lower numbers will be displayed higher up

    # Todo: 1) Make a CLI copy of this in 'Improved Implementation' that 'teaches' basic arithemtic operators
    #       2) Write a simplified CLI version of this in 'Minimum Implementation' that illustrates the use of arithmetic operators

    # 0 for encode, 1 for decode
def _cipher(alphabet:str, key_a:int, key_b:int, plain_text, mode=0):
        # Input Validation
        if not len(alphabet) > 0:
            print("Error. Please provide an alphabet.")
            return
        if len(set(alphabet)) != len(alphabet):
            print("Error. Letters in the alphabet must be unique.")
            return
        for key in key_a, key_b:
            try:
                int_key = int(key)
                if int_key != float(key):
                    raise ValueError
            except ValueError:
                print("Error. Please provide integers for the keys.")
                return
        key_a = int(key_a)
        if gcd(key_a, len(alphabet)) > 1:
            print("Error. The key_a and the length of the alphabet provided must be coprime.")
            return

        # The Validated Parameters
        alphabet:List[str] = list(alphabet)
        key_a:int = int(key_a)
        key_b:int = int(key_b)

        # Ciphering...
        cipher_text = []
        for char in plain_text:
            if char in alphabet:
                if mode == 0:
                    keys1 = key_a*alphabet.index(char)+key_b
                    alphabet_length = len(alphabet)
                    cipher_text.append(alphabet[keys1%alphabet_length])
                else:
                    alphabet_length = len(alphabet)
                    keys2 = modinv*(alphabet.index(char)-key_b)
                    modinv = pow(key_a, -1, alphabet_length) #Note: requires Python 3.8+
                    cipher_text.append(alphabet[keys2%alphabet_length])

            else:
                cipher_text.append(char)
        return ''.join(cipher_text)

if __name__ == "__main__":
    alphabet = string.ascii_lowercase
    print(_cipher(alphabet, 7, 5, "hello", mode=0))
    print(_cipher(alphabet, 7, 5, "potato", mode=0))


