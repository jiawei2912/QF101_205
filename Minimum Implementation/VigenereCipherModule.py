from typing import List
import string

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
    key:List[str] = list(key.lower())

    # plaintext letter corresponds to row
    # key letter corresponds to column
    # Ciphering...
    plain_text = inputText.lower()
    cipher_text = []
    for i in range(len(plain_text)): # For each character
        char = plain_text[i]
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
    print("Result: ", end='')
    print(''.join(cipher_text))

if __name__=="__main__":
    alphabet = string.ascii_lowercase
    cipher("hello", alphabet, "key", mode=0)
    cipher("Hello", alphabet, "key", mode=0)
    # cipher("Hopjy", alphabet, "key", mode=1)
    # cipher("GEEKSFORGEEKS", alphabet, "AYUSH", mode=0)