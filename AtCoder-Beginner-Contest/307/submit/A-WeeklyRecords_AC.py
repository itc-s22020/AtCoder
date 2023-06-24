#[AC] 207Byte 24ms 8892KB Python3
n = int(input())
l = list(map(int, input().split()))

def split_list(l, n):
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]
        
r = [sum(i) for i in split_list(l,7)]
print(*r)

