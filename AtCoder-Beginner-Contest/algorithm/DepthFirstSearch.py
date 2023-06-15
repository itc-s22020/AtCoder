#深さ優先探索(Depth First Search)
N,M = map(int, input().split())

#グラフ作成
def mkGraph(n,m):
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b)
        g[b-1].append(a) #有形グラフの場合はコメントアウト
    return g

#深さ優先探索
G = mkGraph(N,M)
seen = [False for _ in range(len(G))]
def DFS(g, n):
    seen[n] = True
    for v in g[n]:
        if (seen[v]): continue
        DFS(G, v)
    


DFS(G, 0)
print(G)
print(seen)