N = int(input())
t = set()
for _ in range(N):
    S = input()
    t.add(min(S, S[::-1]))
print(len(t))

