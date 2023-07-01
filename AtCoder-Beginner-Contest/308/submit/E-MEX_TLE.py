#[TLE] 622Byte TLE 268972KB Python3
def calculate_mex_sum(N, A, S):
    mex_sum = 0
    mex_counts = {}
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] == 'M' and S[j] == 'E' and S[k] == 'X':
                    mex_val = 0
                    while mex_val in [A[i], A[j], A[k]]:
                        mex_val += 1
                    mex_sum += mex_val
                    mex_counts[(i, j, k)] = mex_val
    return mex_sum, mex_counts

N = int(input())
A = list(map(int, input().split()))
S = input()

mex_sum, mex_counts = calculate_mex_sum(N, A, S)
print(mex_sum)


