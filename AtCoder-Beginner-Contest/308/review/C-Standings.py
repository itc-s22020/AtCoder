from decimal import Decimal, getcontext

def sort_people(N, A, B):
    success_rates = [Decimal(A[i]) / (Decimal(A[i]) + Decimal(B[i])) for i in range(N)]
    sorted_people = sorted(range(1, N+1), key=lambda i: (-success_rates[i-1], i))
    return sorted_people

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# Decimalの精度を設定
getcontext().prec = 28

sorted_people = sort_people(N, A, B)
print(*sorted_people)


