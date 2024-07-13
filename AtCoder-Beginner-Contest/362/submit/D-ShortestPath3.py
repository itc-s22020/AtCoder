from collections import deque
N, M = map(int, input().split())
A = list(map(int, input().split()))
e = [[] for _ in range(N)]
for _ in range(M):
    U, V, B = map(int, input().split())
    U -= 1
    V -= 1
    e[U].append([V, B])
    e[V].append([U, B])
def b():
    dist = [float('inf')] * N
    dist[0] = A[0]
    queue = deque([(0, A[0])])
    while queue:
        v, d = queue.popleft()
        if d > dist[v]:
            continue
        for u, b in e[v]:
            new_d = d + b + A[u]
            if new_d < dist[u]:
                dist[u] = new_d
                queue.append((u, new_d))
    return dist
print(*b()[1:], sep=" ")
