from __future__ import annotations
from typing import List
import random
from math import gcd
import time


# <><> Utility Function <><>
def _isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n < 2:
        return False
    # Worst case scenario: n = n^0.5 X n^0.5 => No need to check beyond sqrt
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

order:int = 70
min_pq:int = 100
max_pq:int = 10_000
primes:List[int] = [i for i in range(min_pq, max_pq+1) if _isPrime(i)]
min_n:int = 10000
max_n:int = 1_000_000
primes:List[int] = [i for i in range(min_pq, max_pq+1) if _isPrime(i)]


def _generate_rsa_key_pair():
    # Draw 2 random primes
    p = q = -1
    while p == q:
        p, q = random.choices(primes, k=2)
        if p*q < min_n or p*q > max_n:
            p = q = -1
    # Calculate n, e, and d
    n = p*q
    phi = (p-1)*(q-1)
    e = -1
    for i in range(2, n):
        if gcd(i, phi) == 1:
            e = i
            break
    d = -1
    for i in range(2, n):
        if i*e % phi == 1:
            d = i
            break
    # Output to UI
    return n, e, d




# 0 for encode, 1 for decode
def _cipher(mode,n,e,d,inputtext):
    # Input Validation
    inputs = [n,e,d]
    if mode == 0: #encrypt
        inputs.pop(2)
    elif mode == 1: #decrypt
        inputs.pop(1)
    for input in inputs:
        try:
            if int(input) != float(input):
                raise ValueError
        except ValueError:
            print("Error. Please provide integers.")
            return
    for char in inputtext:
        if ord(char) > 128:
            print('Error! This implementation only accepts ASCII-characters in its input.')
            return
    if mode == 1:
        for char in inputtext.split(' '):
            try:
                int(char, 16)
            except ValueError:
                print('Error! The input should be hexadecimal.')
                return


    # Ciphering...
    plain_text = inputtext
    cipher_text = []
    if mode == 0:
        for char in plain_text:
            cipher_hex = hex((ord(char)**e)%n)
            cipher_text.append(str(cipher_hex)[2:])      
        return (' '.join(cipher_text))    
    else:
        for char in plain_text.split(' '):
            plain_dec = (int(char, 16)**d)%n
            cipher_text.append(chr(plain_dec))
        return (''.join(cipher_text))  
        



if __name__ == "__main__":
    n,e,d=_generate_rsa_key_pair()
    start = time.time()
    ciphertext = _cipher(0,n,e,d,'i love qf')
    print(ciphertext)
    print(_cipher(1,n,e,d,str(ciphertext)))
    end = time.time()
    print('Time taken: ' + str(end - start)+'s')
    start = time.time()
    ciphertext = _cipher(0,n,e,d,'this is a super long message that might take some time to encrypt and decrypt, i dont know how long but it should take a while lets calculate it with some code')
    print(ciphertext)
    print(_cipher(1,n,e,d,str(ciphertext)))
    end = time.time()
    print('Time taken: ' + str(end - start)+'s')