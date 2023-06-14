#深さ優先探索(Depth First Search)
N,M = map(int, input().split())
def Graph(n,m):
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    return g
G = Graph(N,M)
print()
print(G)
