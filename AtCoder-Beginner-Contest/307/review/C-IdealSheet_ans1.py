def convert(H, W, S):
    s = set()
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                s.add((i, j))
    return s

def normalize(s):
    my = min(y for (y, x) in s)
    mx = min(x for (y, x) in s)
    return set((y - my, x - mx) for (y, x) in s)

HA, WA = map(int, input().split())
A = normalize(convert(HA, WA, [input() for _ in range(HA)]))
HB, WB = map(int, input().split())
B = normalize(convert(HB, WB, [input() for _ in range(HB)]))
HX, WX = map(int, input().split())
X = normalize(convert(HX, WX, [input() for _ in range(HX)]))
ans = False
for dy in range(-HX, HX):
    for dx in range(-WX, WX):
        ans |= normalize(A.union((y + dy, x + dx) for (y, x) in B)) == X
print('Yes' if ans else 'No')

