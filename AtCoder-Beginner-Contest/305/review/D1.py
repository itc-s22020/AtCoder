###提出コード修正 TLE16 AC4
x = int(input())
sui = list(map(int,input().split()))
q = int(input())
W = [ list(map(int,input().split())) for _ in range(q)]

#[睡眠開始時間, 睡眠終了時間]
S = [[sui[i],sui[i+1]] for i in range(len(sui)-1) if i%2!=0]

for v in W:
    total = 0
    for L in S:
        V1,V2 = v[0], v[1]
        L1,L2 = L[0], L[1]

        #時間時間がすべて睡眠時間の場合
        if L1 < V1 < L2 and L1 < V2 < L2:
            total += V2 - V1
            break

        #記録開始,終了時間が睡眠時間内の場合
        if L1 < V1 < L2:
            total += L2 - V1
            continue
        elif L1 < V2 < L2:
            total += V2 - L1
            continue
        
        #上記のいずれも該当しないかつ、睡眠時間の全てが記録範囲内の場合
        if L1 >= V1 and L2 <= V2:
            total += L2 - L1
    print(total)

