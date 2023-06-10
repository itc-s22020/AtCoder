#[AC] 343Byte 30ms 9248KB Python3
x,y = map(int, input().split())
l = [input() for _ in range(x)]
sMax, sMin  = [0,0] , [0,999]
for a in range(x):
    K = l[a]
    KC = [a ,K.count('#')]
    if sMax[1] < KC[1]: sMax = KC
    if sMin[1] > KC[1] > 0: sMin = KC
V = 0
for b in range(y):
    N,M = sMax[0], sMin[0]
    if l[N][b] != l[M][b]:V = b

print(sMin[0]+1,V+1)
