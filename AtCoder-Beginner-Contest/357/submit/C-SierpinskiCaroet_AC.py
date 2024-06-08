S, r = 3 ** (N := int(input())), range
m = [['#' for _ in r(S)] for _ in r(S)]
for i in r(N):
    C = 3 ** i
    for j in r(C, S, C * 3):
        for k in r(C, S, C * 3):
            for l in r(C):
                m[j + l][k:k + C] = ['.'] * C
[print(''.join(r)) for r in m]