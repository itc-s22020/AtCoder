#リスト二分探索
from bisect import bisect_left

N=int(input())
A=list(map(int,input().split()))
Q=int(input())
XY=[list(map(int,input().split())) for _ in range(Q)]
 
#C~Aの累積和
C=[0]*(N+1)
for i in range(1,N):
    if i%2==1:C[i+1]=C[i]+(A[i+1]-A[i])
    else:C[i+1]=C[i]

for X,Y in XY:
    V=0
    #AをXYでポイントチェック 
    pX=bisect_left(A,X)
    pY=bisect_left(A,Y)
    #pXYの偶数判定
    if pX%2==0:V+=A[pX]-X #A[pX]とXの差を加算
    if pY%2==0:V-=A[pY]-Y #A[pY]とYの差を減算
    V+=C[pY]-C[pX] #累積和の差を加算
    print(V)
