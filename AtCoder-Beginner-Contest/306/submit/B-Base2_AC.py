#[AC] 121Byte 21ms 8976KB Python3
nums = list(map(int, input().split()))
V = 0
for i,v in enumerate(nums):
    if v == 1:
        V += 2**i
print(V)

