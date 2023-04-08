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
    # convert key string to list
    key:List[str] = list(key.lower())
    inputText = inputText.lower()

    # offsets a string by an offset
    def slicer(alphabet:str, offset:int)->list:
        return alphabet[offset:] + alphabet[:offset]

    # Create Vigenere table: 2D list where each row is the alphabet, shifted by row number i. 
    # e.g., 1: a,b,c,d 2: b,c,d,a 3: c,d,a,v ....
    vTable:List[List] = [slicer(alphabet, i) for i in range(len(alphabet))]

    cipher_text = []
    for i in range(len(inputText)): # For each character
        # Get the alphabet indices for input and key characters
        iCharIdx, kCharIdx = alphabet.index(inputText[i]), alphabet.index(key[i%len(key)])
        if mode==0: # if encoding
            # Append the character in the Vigenere table corresponding to input and key characters
            cipher_text.append(vTable[kCharIdx][iCharIdx])
        else:  # if decoding
            # Get the alphabet index of the char in the row corresponding to the key character
            oCharIdx = vTable[kCharIdx].index(inputText[i])
            # Convert alphabet index to alphabet char
            cipher_text.append(alphabet[oCharIdx])
    return ''.join(cipher_text)


if __name__=="__main__":
    alphabet = string.ascii_lowercase
    print(cipher("hello", alphabet, "key", mode=0))
    print(cipher("rijvs", alphabet, "key", mode=1))