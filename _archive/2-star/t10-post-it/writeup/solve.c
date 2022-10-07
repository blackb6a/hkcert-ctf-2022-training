#include <bits/stdc++.h>

using namespace std;

// 10 ^ 18 + 3, this way plus wont overflow
#define MOD 1000000000000000003ull

unsigned long long fib(unsigned int i) {
    if (i == 0) {
        return 0;
    }
    unsigned long long prev = 0, val = 1;
    i--;
    for (unsigned int j = 0; j < i; j++) {
        unsigned long long tmp = val;
        val = (val + prev) % MOD;
        prev = tmp;
    }
    return val % MOD;
}

uint key[] = {
    50928, 40749, 9565, 46099, 41782, 13663, 27947, 61296, 29225, 13283,
    37430, 50731, 31795, 3576, 30323, 50276, 44420, 45033, 6161, 37434,
    43354, 37137, 26063, 55410, 17757, 5197, 10497, 65305, 36190, 9589,
    17139, 63125, 26182, 22881, 62993, 19541, 34071, 8824, 43362, 15255,
    53597, 45432, 56954, 33126, 33099, 12915, 57540, 48526, 38230, 2246,
    41792, 43843, 61986, 26259, 1820, 36372, 38254, 56308, 950, 7037,
    23422, 33922, 41248, 63769, 50560, 12846, 27394, 43220
};
char const flag[] = {
    (char)184, (char)36, (char)57, (char)71, (char)72, (char)223, (char)44, (char)241, (char)143, (char)224, (char)243, (char)151, (char)112, (char)203, (char)149, (char)206, (char)120, (char)235, (char)227, (char)175, (char)225, (char)248, (char)130, (char)8, (char)234, (char)103, (char)34, (char)74, (char)44, (char)189, (char)182, (char)63, (char)46, (char)49, (char)78, (char)56, (char)194, (char)144, (char)135, (char)60, (char)101, (char)86, (char)228, (char)144, (char)128, (char)220, (char)124, (char)43, (char)92, (char)4, (char)95, (char)240, (char)145, (char)151, (char)26, (char)147, (char)81, (char)169, (char)17, (char)26, (char)219, (char)159, (char)36, (char)174, (char)8, (char)186, (char)202, (char)44
};

int main() {
    for (int i = 0; i < 68; i++) {
        unsigned long long val = fib(key[i]);
        srand(val % 0xFFFFFFFF);
        int key = rand() % 256;
        cout << char(int(flag[i]) ^ key);
    }
    cout << endl;
}

// flag: hkcert22{d0-y0u-u53-m3m01z4t1oN-0r-ju5t-i7i73r4t1v3-0R-ju5t-g00g13?}
