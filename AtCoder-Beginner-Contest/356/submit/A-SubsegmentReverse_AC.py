data = input().split()
N = int(data[0])
L = int(data[1])
R = int(data[2])

A = list(range(1, N + 1))
A[L-1:R] = A[L-1:R][::-1]
print(" ".join(map(str, A)))
