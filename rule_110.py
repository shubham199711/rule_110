import time
import random

pattern = {
    "111": "0",
    "110": "1",
    "101": "1",
    "100": "0",
    "011": "1",
    "010": "1",
    "001": "1",
    "000": "0",
}

full = "█"
empty = " "
cache = set()

def rule_110(n, code):
    size = len(code)

    code = list(code)
    new = []
    loop = 0
    while loop < n:
        loop += 1
        time.sleep(0.1)
        for index in range(size):
            i = (index-1) % size
            j = index % size
            k = (index+1) % size
            c = ''.join([code[i], code[j], code[k]])
            new.append(pattern[c])
        code = new
        new = []
        p = ''.join([i.replace("0", empty).replace("1", full) for i in code])
        if p in cache:
            break
        cache.add(p)
        print(p)
    return loop

def test():
    code = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100"
    rule_110(100, code)

if __name__ == '__main__':
    test()
