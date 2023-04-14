# pick prime p and q
# find n = p * q
# choose e
# --> e < n
# --> e coprime (p-1)(q-1)
# Find d
# --> d mod (p-1)(q-1) = 1

# public key = e,n
# private key = d,n

# Encryption
# --> c = m^e mod n; Note: m must be less than n
# Decryption
# --> m = c^d mod n
from math import gcd

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n < 2:
        return False
    # Worst case scenario: n = n^0.5 X n^0.5 => No need to check beyond sqrt
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def gen_rsa(p, q):
    if not (isPrime(p) and isPrime(q)):
        print("p and q must be prime.")
        return
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

    print('n:', n)
    print('e:', e)
    print('d:', d)
    pass

def rsa_encrypt(m, e, n):
    print('ciphertext:', (m**e) % n)
    
def rsa_decrypt(c, d, n):
    print('plaintext:', (c**d) % n)

gen_rsa(3, 11) # n=33, e=3, d=7
rsa_encrypt(5, 3, 33)
rsa_decrypt(26, 7, 33)

#gen_rsa(101, 79) # n=7979, e=7, d=3343
# rsa_encrypt(9, 7, 7979) # 3548
# rsa_decrypt(3548, 3343, 7979)

# primes = []
# for i in range(10_000, 100_000+1):
#     if isPrime(i):
#         primes.append(i)
# print(primes)


# 8 bits per ASCII char
# n must be at least 128 to encrypt 1 ASCII char
# n should probably be less than 10000 for computation reasons