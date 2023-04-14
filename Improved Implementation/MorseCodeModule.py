ALPHANUM_2_MORSE_CODE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    0: '-----',
    1: '.----',
    2: '..---',
    3: '...--',
    4: '....-',
    5: '.....',
    6: '-....',
    7: '--...',
    8: '---..',
    9: '----.'
}

MORSE_CODE_2_ALPHANUM = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '-----': 0,
    '.----': 1,
    '..---': 2,
    '...--': 3,
    '....-': 4,
    '.....': 5,
    '-....': 6,
    '--...': 7,
    '---..': 8,
    '----.': 9
}


def encode(plainText):
    cipher_text = []
    for char in plainText:
        if char in ALPHANUM_2_MORSE_CODE:
            cipher_text.append(ALPHANUM_2_MORSE_CODE[char])
        elif char == ' ':
            cipher_text.append(' / ')
        else:
            cipher_text.append(char)
    return ' '.join(cipher_text)

def decode(plainText):
    cipher_text = []
    for char in plainText.split():
        if char in MORSE_CODE_2_ALPHANUM:
            cipher_text.append(MORSE_CODE_2_ALPHANUM[char])
        elif char == '/':
            cipher_text.append(' ')
        else:
            cipher_text.append(char)
    return ''.join(cipher_text)

#more better encode
def encode(plainText):
    return ' '.join(ALPHANUM_2_MORSE_CODE[char] if char in ALPHANUM_2_MORSE_CODE 
                    else ' /' if char == ' ' else char
                    for char in plainText)

# more better decode
def decode(plainText):
    return ''.join(MORSE_CODE_2_ALPHANUM[char] if char in MORSE_CODE_2_ALPHANUM
                   else ' ' if char == '/' else char
                   for char in plainText.split())


if __name__ == "__main__":
    print(encode("my pony flies over the ocean, my pony lies over the sea"))
    print(decode("-- -.--  /  .--. --- -. -.--  /  ..-. .-.. .. . ...  /  --- ...- . .-.  /  - .... .  /  --- -.-. . .- -. ,  /  -- -.--  /  .--. --- -. -.--  /  .-.. .. . ...  /  --- ...- . .-.  /  - .... .  /  ... . .-"))
