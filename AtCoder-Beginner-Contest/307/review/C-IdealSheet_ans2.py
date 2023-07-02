def I():
    h, w = map(int, input().split())
    s = 0
    for _ in range(h):
        s = (s << 20) + int(input().replace("#", "1").replace(".", "0"), 2)
    return s // (s & -s)

a, b, x = I(), I(), I()
for i in range(300):
    if a | (b << i) == x or (a << i) | b == x:
        print("Yes")
        break
else:
    print("No")
