from typing import List
import string
import pprint

# Todo: 1) Remove the use of the Class and the GUI
#       2) You can use functions
#       3) Simplify this into a standalone file

# Each AppModule needs to have:
#   self.title: display name of the module
#   self.order: ordering priority; lower numbers will be displayed higher up

    # Todo: 1) Make a CLI copy of this in 'Improved Implementation' that 'teaches' 2D lists
    #       2) Write a simplified CLI version of this in 'Minimum Implementation' that illustrates the use of a 2D list

    # 0 for encode, 1 for decode
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

    # Create 2D list where each row is the alphabet, shifted by row number i. 
    # e.g., 1: a,b,c,d 2: b,c,d,a 3: c,d,a,v ....
    table:List[List] = [(lambda a, i: a[i:] + a[:i])(alphabet, i) for i in range(len(alphabet))]

    cipher_text = []
    for i in range(len(inputText)): # For each character
        # Get the alphabet indices for input and key characters
        iCharIdx, kCharIdx = alphabet.index(inputText[i]), alphabet.index(key[i%len(key)])
        if mode==0: # if encoding
            # Append the character in the Vigenere table corresponding to input and key characters
            cipher_text.append(table[kCharIdx][iCharIdx])
        else:  # if decoding
            # Get the alphabet index of the char in the row corresponding to the key character
            oCharIdx = table[kCharIdx].index(inputText[i])
            # Convert alphabet index to alphabet char
            cipher_text.append(alphabet[oCharIdx])
    return ''.join(cipher_text)


if __name__=="__main__":
    alphabet = string.ascii_lowercase
    print(cipher("Hello", alphabet, "key", mode=0))
    # print(cipher("GEEKSFORGEEKS", alphabet, "AYUSH", mode=0))
    print(cipher("rijvs", alphabet, "key", mode=1))
    # cipher("Hopjy", alphabet, "key", mode=1)
    # def shift(alphabet: List, i):
    #     return alphabet[i:] + alphabet[:i]
    # print(shift(alphabet, 0))