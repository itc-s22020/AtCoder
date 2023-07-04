n, m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))
ans = 0
for v in c:
    price = p[0]
    for j in range(m):
        if v == d[j]:
            price = p[j + 1]
            break
    ans += price
print(ans)

