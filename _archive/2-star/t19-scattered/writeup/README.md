The challenge can be done in two ways, the easier way is to do this dynamically (using debugger); while the hard way is to do this statically.

Running it prints the following:
```
Hello world!
Seems putting flag in binary will leak flag easily...
I heard string obfuscation can prevent that :thinking:
Now I obfuscate all the strings, find me if you can!
```

This seems to suggest the flag is obfuscated and lives inside the binary.

Using `strings` on the binary dont give us any flags, but we can clearly see the symbol is not stripped.

Some interest function name is, e.g. `_ZN2ay15obfuscated_dataILy33ELy16840563957759296883EED2Ev`, which if you put it into demangler (or just look in decompiler like IDA), it is something
like `ay::obfuscated_data<33ull, 16840563957759296883ull>::~obfuscated_data()`, which can be googled and leads to [adamyaxley/Obfuscate](https://github.com/adamyaxley/Obfuscate).

By looking into the github we can see this is a compile time string obfuscator using XOR.

The hard-way will be to retrieve the XOR key and the raw data, and write some simple script to deobfuscate the strings.

But we can do it much simpler using dynamic analysis. This is because the program will deobfuscate the string in runtime (so the program can actually use those strings).

As there is symbol, we can just do `break main` in `gef`. (if the binary is stripped, we can look for the address in decompiler (e.g. IDA))

Then, as we know the format of the flag contains `hkcert`, we can just do `find hkcert` to try to search for the string in memory.

```
gef> find hkcert
[+] Searching 'hkcert' in memory
[+] In '/home/harrier/ctf/hkcert/22/hkcert-ctf-2022-training-internal/t19-scattered/public/strings'(0x603000-0x604000), permission=rw-
  0x6031b0 - 0x6031b6  ->   "hkcert"
[+] In '[stack]'(0x7ffffffde000-0x7ffffffff000), permission=rw-
  0x7fffffffe28e - 0x7fffffffe294  ->   "hkcert"
  0x7fffffffe298 - 0x7fffffffe29e  ->   "hkcert"
  0x7fffffffe33f - 0x7fffffffe345  ->   "hkcert"
  0x7fffffffe349 - 0x7fffffffe34f  ->   "hkcert"
  0x7fffffffeed3 - 0x7fffffffeed9  ->   "hkcert"
  0x7fffffffeedd - 0x7fffffffeee3  ->   "hkcert"
  0x7fffffffefaf - 0x7fffffffefb5  ->   "hkcert"
  0x7fffffffefb9 - 0x7fffffffefbf  ->   "hkcert"
```

The deobfuscated string will be in one of the segments in the file (and probably not on the stack).

But looking into the first entry gives us the flag:

```
gef> der 0x6031b0
0x00000000006031b0|+0x0000(000): 'hkcert21{str_0bfU5c4t1oN_x0r_X0r'
0x00000000006031b8|+0x0008(001): '{str_0bfU5c4t1oN_x0r_X0r'
0x00000000006031c0|+0x0010(002): 'U5c4t1oN_x0r_X0r'
0x00000000006031c8|+0x0018(003): '_x0r_X0r'
0x00000000006031d0|+0x0020(004): 0x0000000000000000
0x00000000006031d8|+0x0028(005): 0x0000000000000001
0x00000000006031e0|+0x0030(006): '_w1tH_d3t3rm1n1st1c_h45h3s}'
0x00000000006031e8|+0x0038(007): 't3rm1n1st1c_h45h3s}'
0x00000000006031f0|+0x0040(008): 't1c_h45h3s}'
0x00000000006031f8|+0x0048(009): 0x00000000007d7333 ('3s}'?)
```
