_,P,Q = map(int, input().split())
li = sorted(map(int, input().split()))
Ql = li[0] + Q
print((P , Ql)[P > Ql])
