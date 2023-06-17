#[TLE] 340Byte 2206ms 43688KB Python3
n = int(input())
nums = list(map(int, input().split()))
def f(n,l):
    li = []
    for i,v in enumerate(l):
        if v == n:
            li.append(i+1)
    return li[1]

dic = {}
for i in range(n):
    d = {str(i+1): f(i+1,nums)}
    dic.update(d)
V = sorted(dic.items(), key=lambda x:x[1])
K = [i[0] for i in V]
print(*K)
