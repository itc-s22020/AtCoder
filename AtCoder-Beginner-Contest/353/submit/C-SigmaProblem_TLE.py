N = int(input())
A = list(map(int, input().split()))

t = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        t += (A[i] + A[j]) % (10 ** 8)

print(t)