S = input()
lc = sum(1 for c in S if c.islower())
uc = len(S) - lc
print(S.upper()) if uc > lc else print(S.lower())
