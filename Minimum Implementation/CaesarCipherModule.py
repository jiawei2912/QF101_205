def cipher(plainText: str,shift: int, mode: int):
    if int(shift) != float(shift) or shift > 2:
        print("Error, please use an integer that is 1 or 2 for shift")
        return
    
    result = ''
    for char in plainText:
        if shift == 1:
            if mode == 0: # ciphering
                if char == 'a':
                    result = result + 'b'
                elif char =='b':
                    result = result + 'c'
                elif char == 'c':
                    result = result + 'd'
                elif char == 'd':
                    result = result + 'e'
                elif char == 'e':
                    result = result + 'a'
                else:
                    result = result + char
            else: # deciphering
                if char == 'a':
                    result = result + 'e'
                elif char =='b':
                    result = result + 'a'
                elif char == 'c':
                    result = result + 'b'
                elif char == 'd':
                    result = result + 'c'
                elif char == 'e':
                    result = result + 'd'
                else:
                    result = result + char
        if shift == 2:
            if mode == 0: # ciphering
                if char == 'a':
                    result = result + 'c'
                elif char =='b':
                    result = result + 'd'
                elif char == 'c':
                    result = result + 'e'
                elif char == 'd':
                    result = result + 'a'
                elif char == 'e':
                    result = result + 'b'
                else:
                    result = result + char
            else: #deciphering
                if char == 'a':
                    result = result + 'd'
                elif char =='b':
                    result = result + 'e'
                elif char == 'c':
                    result = result + 'a'
                elif char == 'd':
                    result = result + 'b'
                elif char == 'e':
                    result = result + 'c'
                else:
                    result = result + char
    
    return result

if __name__=="__main__":
    print(cipher("becca", 1, mode=0))
    print(cipher("caddb", 1, mode=1))