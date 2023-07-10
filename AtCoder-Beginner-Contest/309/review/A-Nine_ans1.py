A, B = map(int, input().split())
ra, ca = (A - 1) // 3, (A - 1) % 3
rb, cb = (B - 1) // 3, (B - 1) % 3
print('Yes' if ra == rb and ca + 1 == cb else 'No')

