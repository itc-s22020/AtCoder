#[WA] 398Byte 693ms 62656KB Python3
def sort_people(N, A, B):
    success_rates = [float(A[i]) / (A[i] + B[i]) for i in range(N)]
    sorted_people = sorted(range(1, N+1), key=lambda i: (-success_rates[i-1], i))
    return sorted_people

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

sorted_people = sort_people(N, A, B)
print(*sorted_people)


