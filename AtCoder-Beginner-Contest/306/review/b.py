#提出したコードの修正
nums = list(map(int, input().split()))
V = [(0,2**i)[v==1] for i, v in enumerate(nums)]
print(sum(V))
