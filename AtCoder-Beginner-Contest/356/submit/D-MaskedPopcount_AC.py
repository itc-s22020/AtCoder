MOD = 998244353
N, M = map(int, input().split())

result = 0

for i in range(61):
    if M & (1 << i):
        p = 1 << (i + 1)
        f = N // p
        r = N % p
        c = f * (1 << i)
        c += max(0, r - (1 << i) + 1)
        result = (result + c) % MOD

print(result)

