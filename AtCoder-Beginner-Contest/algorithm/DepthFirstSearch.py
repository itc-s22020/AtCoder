#深さ優先探索(Depth First Search)
N,M = map(int, input().split())

#グラフ作成
def mkGraph(n,m,T):
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b)
        if (T): g[b-1].append(a) #有形グラフの場合はコメントアウト
    return g

#深さ優先探索
G = mkGraph(N,M,False)
seen = [False for _ in range(len(G))]
def DFS(g, v):
    seen[v-1] = True #探索済にする
    # v から到達可能な next_v について
    for next_v in g[v-1]:
        if (seen[next_v-1]): continue # next_v が探索済ならスルー
        DFS(G, next_v) #再帰処理


DFS(G, 1)
print(("NO", "YES")[seen[9]]) #頂点0から頂点9に辿り着けるか
print(seen)