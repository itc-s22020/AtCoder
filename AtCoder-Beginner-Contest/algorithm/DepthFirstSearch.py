#深さ優先探索(Depth First Search)
N,M = map(int, input().split())

#グラフ作成
def mkGraph(n,m,T):
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b)
        if (T): g[b-1].append(a) #無形グラフならappend
    return g

#深さ優先探索
G = mkGraph(N,M,False)
seen = [False for _ in range(len(G))]
def DFS(g, v):
    seen[v-1] = True #探索済にする
    # v から到達可能な next_v について
    for next_v in g[v-1]:
        if (seen[next_v-1]): continue # next_v が探索済ならスルー
        DFS(g, next_v) #再帰処理

#頂点sが頂点vに到達可能か
def StoV(g,s,v):
    DFS(g, s)
    print(("NO", "YES")[seen[v-1]])

StoV(G,1,10) #頂点1から頂点10に到達可能？
StoV(G,2,10) #頂点2から頂点10に到達可能？