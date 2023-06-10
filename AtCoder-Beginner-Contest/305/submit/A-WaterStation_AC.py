#[AC] 140Byte 23ms 9072KB Python3

a = int(input())
e = a % 5
b = a // 5
if e == 0:
    print(a)
else:
    if e > 2:
        print(b*5+5)
    else:
        print(b*5)
