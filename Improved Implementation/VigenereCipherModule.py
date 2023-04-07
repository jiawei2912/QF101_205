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
    key = key * (len(inputText)//len(key)+1)
    key:List[str] = list(key.lower())
    inputText = inputText.lower()

    alphIndex = {a:i for i, a in enumerate(alphabet)}
    # A 2D list
    table:List[List] = [(lambda a, i: a[i:] + a[:i])(alphabet, i) for i in range(len(alphabet))]

    cipher_text = []
    for i in range(len(inputText)):
        iChar, kChar = alphIndex[inputText[i]], alphIndex[key[i]]
        if mode==0:
            cipher_text.append(table[kChar][iChar])
        else: 
            tIndex = table[kChar].index(inputText[i])
            cipher_text.append(alphabet[tIndex])
    return ''.join(cipher_text)


    # for t in table:
    #     print(t)

    # plaintext letter corresponds to row
    # key letter corresponds to column
    # Ciphering...
    
    # plain_text = inputText
    # cipher_text = []
    # key_idx = 0
    # for i in range(len(plain_text)):
    #     char = plain_text[i]
    #     key_char = key[key_idx%len(key)]
    #     if char in alphabet:
    #         if mode == 0:
    #             cipher_text.append(alphabet[(alphabet.index(char)+alphabet.index(key_char))%len(alphabet)])
    #         else:
    #             # to decode, find where you are in the column and minus by idx of key_char in alphabet
    #             cipher_text.append(alphabet[(alphabet.index(char)-alphabet.index(key_char))])
    #         key_idx+=1
    #     else:
    #         cipher_text.append(char)
    # print("Result: ", end='')
    # print(''.join(cipher_text))

if __name__=="__main__":
    alphabet = string.ascii_lowercase
    print(cipher("Hello", alphabet, "key", mode=0))
    # print(cipher("GEEKSFORGEEKS", alphabet, "AYUSH", mode=0))
    print(cipher("rijvs", alphabet, "key", mode=1))
    # cipher("Hopjy", alphabet, "key", mode=1)
    # def shift(alphabet: List, i):
    #     return alphabet[i:] + alphabet[:i]
    # print(shift(alphabet, 0))