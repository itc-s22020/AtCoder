#[TLE] 724Byte 3309ms 54704KB Python3
x = int(input())
sui = list(map(int,input().split()))
q = int(input())
W = [ list(map(int,input().split())) for _ in range(q)]

for i, v in enumerate(W):
    total = 0
    E = 0
    J = 0
    for l in range(len(sui)-1):
        O, I = sui[l], sui[l+1]
        if l % 2 != 0:
            if O < v[0] < I and O < v[1] < I:
                total += v[1] - v[0]
                break
            if O < v[0] < I:
                E = sui[l+1] - v[0]
                total += E
                continue
            if O < v[1] < I:
                J = v[1] - sui[l]
                total += J
                continue
            if O >= v[0] and I <= v[1]:
                total += I - O
    print(total)
