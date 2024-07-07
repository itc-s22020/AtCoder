a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
print("Yes") if max(0, min(d, j) - max(a, g)) > 0 and max(0, min(e, k) - max(b, h)) > 0 and max(0, min(f, l) - max(c, i)) > 0 else print("No")
