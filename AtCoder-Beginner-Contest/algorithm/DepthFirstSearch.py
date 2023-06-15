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
first = [0 for _ in range(len(G))]
def DFS(g, v, f):
    #行きがけ順をメモ
    first[v-1] += f
    f += 1
    
    seen[v-1] = True #探索済にする
    # v から到達可能な next_v について
    for next_v in g[v-1]:
        if (seen[next_v-1]): continue # next_v が探索済ならスルー
        DFS(G, next_v, f) #再帰処理


F = 0
DFS(G, 0, F)
print(seen)
print(first)