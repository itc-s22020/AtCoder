N, K, X = map(int, input().split())
A = list(map(int, input().split()))
B = A[:K] + [X] + A[K:]
print(' '.join(map(str, B)))
