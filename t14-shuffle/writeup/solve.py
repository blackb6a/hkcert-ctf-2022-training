import random

def reverse_shuffle(c: int):
    const = [0, 1, 2, 3, 4, 5, 6, 7]
    random.shuffle(const) # [3, 0, 1, 2,. ...]
    shuffled = list(map(int, bin(c)[2:].rjust(8, '0')))
    original = [0, 0, 0, 0, 0, 0, 0, 0]
    for i, pos in enumerate(const):
        original[pos] = shuffled[i]
    return bytes([int("".join(map(str, original)), 2)])

output = b'p\xbcl\xf0Y3C#\xf5\xf8\xb0\xe6\x98%\x17\xaf\xa8\x1d\xf1\x19\xb3i\x9aj\x1e\xccx\xb7F\xea\xfa]\r\xf1X\xc1\x8e\xee'

random.seed(len(output))

flag = b""
for c in output:
    flag += reverse_shuffle(c)

print(flag)

