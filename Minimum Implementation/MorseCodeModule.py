from __future__ import annotations
from typing import List
import string



ALPHABET_MORSE_CODE = [
    '.-',
    '-...',
    '-.-.',
    '-..',
    '.',
    '..-.',
    '--.',
    '....',
    '..',
    '.---',
    '-.-',
    '.-..',
    '--',
    '-.',
    '---',
    '.--.',
    '--.-',
    '.-.',
    '...',
    '-',
    '..-',
    '...-',
    '.--',
    '-..-',
    '-.--',
    '--..'
]

NUMBER_MORSE_CODE = [
    '-----',
    '.----',
    '..---',
    '...--',
    '....-',
    '.....',
    '-....',
    '--...',
    '---..',
    '----.'
]

    # Todo: 1) Make a CLI copy of this in 'Improved Implementation' that 'teaches' Dict
    #       2) Write a simplified CLI version of this in 'Minimum Implementation' that illustrates the use of a Dict

def encode(plainText):
    cipher_text = []
    for char in plainText:
        if ord(char) >= 97 and ord(char) < 97+26:
            cipher_text.append(ALPHABET_MORSE_CODE[ord(char)-97])
        elif ord(char) >= 48 and ord(char) < 48+10:
            cipher_text.append(NUMBER_MORSE_CODE[ord(char)-48])
        elif char == ' ':
            cipher_text.append(' / ')
        else:
            cipher_text.append(char)
    return ' '.join(cipher_text)

def decode(plainText):
    cipher_text = []
    for char in plainText.split():
        if char in ALPHABET_MORSE_CODE:
            cipher_text.append(chr(ALPHABET_MORSE_CODE.index(char) + 97))
        elif char in NUMBER_MORSE_CODE:
            cipher_text.append(chr(NUMBER_MORSE_CODE.index(char) + 48))
        elif char == '/':
            cipher_text.append(' ')
        else:
            cipher_text.append(char)
    return ''.join(cipher_text)

if __name__=="__main__":
    print(encode("becca"))
    print(decode("-... . -.-. -.-. .-"))