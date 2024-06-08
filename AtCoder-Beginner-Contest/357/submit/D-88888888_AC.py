MOD = 998244353
a = pow(10, len(str(N := int(input()))), MOD)
print(
    (((pow(a, N, MOD) - 1) % MOD * pow((a - 1) % MOD, MOD - 2, MOD)) % MOD * N) % MOD
)