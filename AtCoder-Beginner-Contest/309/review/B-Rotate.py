n = int(input())
matrix = [list(map(int, list(input()))) for _ in range(n)]

def rotate(matrix, n):
    v = [[0 for _ in range(n)] for _ in range(n)]
    #リストの上辺下辺処理
    v[0][1:] = matrix[0][:-1]
    v[0][0] = matrix[1][0]
    v[n-1][:-1] = matrix[n-1][1:]
    v[n-1][-1] = matrix[n-2][-1]
    for i in range(1, n-1):
        v[i][0] = matrix[i+1][0]
        v[i][-1] = matrix[i-1][-1]
        v[i][1:-1] = matrix[i][1:-1] 
    return v
v = rotate(matrix, n)
#出力
for i in v:
    l = list(map(str, i))
    print(''.join(l))
