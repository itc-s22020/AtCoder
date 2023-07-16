N,M = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

for v in items:
    for item in items:
        v0, i0, v2, i2 = v[0], item[0], v[2:], item[2:]
        check = set(v2).issubset(i2)
        if (check and v2 != i2 and v0 == i0) or (check and v0 > i0):
            print("Yes")
            exit()
print("No")
