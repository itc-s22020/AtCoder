N,M = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

for v in items:
    for item in items:
        if set(v[2:]).issubset(item[2:]) and v[2:] != item[2:] and v[0] == item[0]:
            print("Yes")
            exit()
        if v[0] <= item[0]:continue
        if set(v[2:]).issubset(item[2:]):
            print("Yes")
            exit()
print("No")
