N, M = map(int, input().split())
A = list(map(int, input().split()))
X = []
for _ in range(N):
    X.append(list(map(int, input().split())))
total = [0] * M
for food in X:
    for j in range(M):
        total[j] += food[j]
a = all(total[j] >= A[j] for j in range(M))
print("Yes") if a else print("No")

