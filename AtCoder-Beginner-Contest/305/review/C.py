#提出したコード
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

#別解(#が2つ以上ある.位置で判定)
x,y = map(int, input().split())
l = [list(input()) for _ in range(x)]
for i in range(x):
    if l[i].count("#")<1: continue
    for j in range(y):
        if l[i][j] == '.':
            c = 0
            # 上下左右判定
            if i != 0 and l[i-1][j] == '#':c += 1
            if i != x-1 and l[i+1][j] == '#':c += 1
            if j != 0 and l[i][j-1] == '#':c += 1
            if j != y-1 and l[i][j+1] == '#':c += 1

            if c >= 2:
                print(i+1, j+1)
                exit()
