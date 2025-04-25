import math 
import random

# Custom RSA 
# By Mikhael

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        r = pow(a, n - 1, n)
        if r != 1:
            return False
    return True

def generate_large_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m_0, x_0, x_1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x_0, x_1 = x_1 - q * x_0, x_0

    if a == 1:
        return x_1 + m_0 if x_1 < 0 else x_1
    return None    

def generate_keypair(bits=1024):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    print("p%q generated.\n")
    n = p * q
    phi = (p - 1) * (q - 1)
    print("n%phi_n generated\n")
    
    e = random.randrange(2, phi-1)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi-1)
    print("pub generated\n")
    d = mod_inverse(e, phi)
    print("priv generated\n")
    pub = (e, n)
    priv = (d, n)
    return pub, priv

def encrypt(plaintext, key):
    k, n = key
    number_array = [ord(char) for char in plaintext]
    cipher_array = [pow(num, k, n) for num in number_array]
    return cipher_array

def decrypt(ciphertext, key):
    k, n = private_key
    plaintext = [pow(char, k, n) for char in ciphertext]
    return "".join([chr(char) for char in plaintext])

if __name__ == '__main__':
    public_key, private_key = generate_keypair()
    print("Keys Generated.\n")
    message = "OTMK"
    
    encrypted_msg = encrypt(message, public_key)
    decrypted_msg = decrypt(encrypted_msg, private_key)
    print("Original message:", message)
    print("Encrypted message:", encrypted_msg)
    print("Decrypted message:", decrypted_msg)
