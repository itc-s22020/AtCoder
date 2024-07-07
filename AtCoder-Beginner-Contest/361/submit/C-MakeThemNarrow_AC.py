N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
r = float('inf')
M=N-K
for i in range(N - M + 1):
    r = min(r, A[i + M - 1] - A[i])
print(r)

