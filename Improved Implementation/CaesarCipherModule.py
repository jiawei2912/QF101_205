from __future__ import annotations
from typing import List
import string

# Method 1: List Append
def cipher(plainText, alphabet, shift, mode=0):
    # Input Validation
    if not len(alphabet) > 0:
        print("Error. Please provide an alphabet.")
        return
    if len(set(alphabet)) != len(alphabet):
        print("Error. Letters in the alphabet must be unique.")
        return
    try:
        int_shift = int(shift)
        if int_shift != float(shift):
            raise ValueError
    except ValueError:
        print("Error. Please provide an integer for shift.")
        return
    shift = int(shift)

    # Mode Switching
    if mode == 1:
        shift *= -1

    # The Validated Parameters
    alphabet:List[str] = list(alphabet)
    shift:int = shift%len(alphabet)

    # (De)Ciphering...
    cipher_text = []
    for char in plainText:
        if char in alphabet:
            cipher_text.append(alphabet[(alphabet.index(char)+shift)%len(alphabet)])
        else:
            cipher_text.append(char)
    return ''.join(cipher_text)

# Method 2: List + List
def cipher(plainText, alphabet, shift, mode=0):
    # Input Validation
    if not len(alphabet) > 0:
        print("Error. Please provide an alphabet.")
        return
    if len(set(alphabet)) != len(alphabet):
        print("Error. Letters in the alphabet must be unique.")
        return
    try:
        int_shift = int(shift)
        if int_shift != float(shift):
            raise ValueError
    except ValueError:
        print("Error. Please provide an integer for shift.")
        return
    shift = int(shift)

    # Mode Switching
    if mode == 1:
        shift *= -1

    # The Validated Parameters
    alphabet:List[str] = list(alphabet)
    shift:int = shift%len(alphabet)

    # (De)Ciphering...
    cipher_text = []
    for char in plainText:
        if char in alphabet:
            cipher_text = cipher_text + [alphabet[(alphabet.index(char)+shift)%len(alphabet)]]
        else:
            cipher_text = cipher_text + [char]
    return ''.join(cipher_text)

# Method 3: List += List
def cipher(plainText, alphabet, shift, mode=0):
    # Input Validation
    if not len(alphabet) > 0:
        print("Error. Please provide an alphabet.")
        return
    if len(set(alphabet)) != len(alphabet):
        print("Error. Letters in the alphabet must be unique.")
        return
    try:
        int_shift = int(shift)
        if int_shift != float(shift):
            raise ValueError
    except ValueError:
        print("Error. Please provide an integer for shift.")
        return
    shift = int(shift)

    # Mode Switching
    if mode == 1:
        shift *= -1

    # The Validated Parameters
    alphabet:List[str] = list(alphabet)
    shift:int = shift%len(alphabet)

    # (De)Ciphering...
    cipher_text = []
    for char in plainText:
        if char in alphabet:
            cipher_text += [alphabet[(alphabet.index(char)+shift)%len(alphabet)]]
        else:
            cipher_text += [char]
    return ''.join(cipher_text)
# Method 4: List.extend(list)
def cipher(plainText, alphabet, shift, mode=0):
    # Input Validation
    if not len(alphabet) > 0:
        print("Error. Please provide an alphabet.")
        return
    if len(set(alphabet)) != len(alphabet):
        print("Error. Letters in the alphabet must be unique.")
        return
    try:
        int_shift = int(shift)
        if int_shift != float(shift):
            raise ValueError
    except ValueError:
        print("Error. Please provide an integer for shift.")
        return
    shift = int(shift)

    # Mode Switching
    if mode == 1:
        shift *= -1

    # The Validated Parameters
    alphabet:List[str] = list(alphabet)
    shift:int = shift%len(alphabet)

    # (De)Ciphering...
    cipher_text = []
    for char in plainText:
        if char in alphabet:
            cipher_text.extend([alphabet[(alphabet.index(char)+shift)%len(alphabet)]])
        else:
            cipher_text.extend([char])
    return ''.join(cipher_text)

# Method 5: List comprehension
def cipher(plainText, alphabet, shift, mode=0):
    # Input Validation
    if not len(alphabet) > 0:
        print("Error. Please provide an alphabet.")
        return
    if len(set(alphabet)) != len(alphabet):
        print("Error. Letters in the alphabet must be unique.")
        return
    try:
        int_shift = int(shift)
        if int_shift != float(shift):
            raise ValueError
    except ValueError:
        print("Error. Please provide an integer for shift.")
        return
    shift = int(shift)

    # Mode Switching
    if mode == 1:
        shift *= -1

    # The Validated Parameters
    alphabet:List[str] = list(alphabet)
    shift:int = shift%len(alphabet)

    # (De)Ciphering...
    cipher_text = [alphabet[(alphabet.index(char)+shift)%len(alphabet)] 
                   if char in alphabet else char 
                   for char in plainText]

    return ''.join(cipher_text)

if __name__=="__main__":
    alphabet = string.ascii_lowercase
    print(cipher("hello", alphabet, 5, mode=0))
    print(cipher("mjqqt", alphabet, 5, mode=1))