import random
import math 

def is_prime(n):
	if n < 2:
		return
	for i in range(2, n // 2+1):
		if n % i == 0:
			return False
	return True

#def gen_prime(min, max):
#Euler's function, for prime numbers
#	p = random.randint(min, max)
#	while not is_prime(p):
#		prime=random.randint(min, max)
#	return p

def mod_inverse(e, phi):
	for d in range(3, phi):
		if (d* e) % phi ==1:
			return d
	raise ValueError("mod_inverse doesn't exist")

#p, q = gen_prime(1000, 5000), gen_prime(1000, 5000)
#while p==q:
#	q = gen_prime(1000, 5000)

p=11
q=13

n = p * q

phi_n = (p-1) * (q-1)

#e = random.randint(3, phi_n-1)
#while math.gcd(e, phi_n) != 1:
#	e = random.randint(3, phi_n-1)

e = 7
d = mod_inverse(e, phi_n)

print(f"Public key: {e}")
print(f"Private key: {d}")
print(f"Phi, of N: {phi_n}")
print(f"P: {p}")
print(f"Q: {q}")

msg = "Hello"

msg_encoded = [ord(c) for c in msg]

cipher = [pow(c,e,n) for c in msg_encoded]

print(f"Message: {msg}")
print(f"Encoded Message: {msg_encoded}")
print(f"Cipher: {cipher}")

decrypt = [pow(ch, d,n) for ch in cipher]
decrypted = "".join(chr(ch) for ch in decrypt)
print(decrypted)
