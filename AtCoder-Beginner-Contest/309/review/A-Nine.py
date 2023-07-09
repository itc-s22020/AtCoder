A, B = map(int, input().split())
def check(a, b):
    if a in [2,5,8] and (a-1 == b or a+1 == b):
        print("Yes")
        exit()
check(A, B)
check(B, A)
print("No")
