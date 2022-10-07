from pwn import *

def xor(a, b):
    return bytes([u^v for u, v in zip(a, b)])

r = remote('localhost', 28109)

# counts[p][c] = number of occurrances of the p-th position of the ciphertext
# being the c-th letter in the alphabet.
counts = [[0 for _ in range(26)] for _ in range(16)]

# Retrieves 1000 ciphertexts from the server.
for _ in range(1000):
    r.sendlineafter(b'> ', b'e')
    ciphertext = r.recvline().strip()

    for k in range(16):
        counts[k][ciphertext[k] - 65] += 1

password = ''
for c in counts:
    # The key k=0 is generated twice likely than the rest.
    c_max = max(c)
    k = c.index(c_max)

    p = chr(k + 65)
    password += p

# Sends the password to the server.
r.sendlineafter(b'> ', b'g')
r.sendlineafter(b'> ', password)

r.interactive()
