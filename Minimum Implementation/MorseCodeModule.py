from __future__ import annotations



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