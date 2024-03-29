from typing import List
import string

def cipher(inputText:str, alphabet:str, key:str, mode=0):
    # Input Validation
    if not len(alphabet) > 0:
        print("Error. Please provide an alphabet.")
        return
    if len(set(alphabet)) != len(alphabet):
        print("Error. Letters in the alphabet must be unique.")
        return
    if not len(key) > 0:
        print("Error. Please provide a key.")
        return
    for char in key:
        if not char in alphabet:
            print("Error. Letters in the key must exist in the alphabet.")
            return

    # The Validated Parameters
    alphabet:List[str] = list(alphabet.lower())
    key:List[str] = list(key.lower())
    inputText = inputText.lower()

    # plaintext letter corresponds to row
    # key letter corresponds to column
    
    cipher_text = []
    for i in range(len(inputText)): # For each character
        char = inputText[i]
        # Get key character per index
        key_char = key[i%len(key)]
        if char in alphabet:
            if mode == 0:
                # Get the alphabet indices for input and key characters
                iChar, kChar = alphabet.index(char), alphabet.index(key_char)
                # Get the index of the output character
                oCharIdx = (iChar + kChar)%len(alphabet)
                # Convert alphabet index into alphabet char
                cipher_text.append(alphabet[oCharIdx])
            else:
                # to decode, find where you are in the column and minus by idx of key_char in alphabet
                oCharIdx = alphabet.index(char)-alphabet.index(key_char)
                cipher_text.append(alphabet[oCharIdx])
        else:
            cipher_text.append(char)
    return ''.join(cipher_text)

if __name__=="__main__":
    alphabet = string.ascii_lowercase
    print(cipher("hello", alphabet, "key", mode=0))
    print(cipher("rijvs", alphabet, "key", mode=1))