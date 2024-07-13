R, G, B = map(int, input().split())
C = input().strip()
if C == "Red":r = min(G, B)
elif C == "Green":r = min(R, B)
else: r = min(R, G)
print(r)

