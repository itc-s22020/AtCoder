#[AC] 235Byte 25ms 9168KB Python3
N = int(input())
na = [list(input().split()) for _ in range(N)]
lname = [name for name,_ in na]
lnum = [int(num) for _,num in na]

Imin = lnum.index(min(lnum))

L = lname[Imin:]
R = lname[:Imin]
print(*L, end=" ")
print(*R)