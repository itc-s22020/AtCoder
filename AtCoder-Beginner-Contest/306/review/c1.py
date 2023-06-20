#提出コードの修正
num = int(input())
nums = list(map(int, input().split()))

dic = {}
for n in range(num):
    li = []
    U = 0
    for i in range(len(nums)):
        if nums[i] == n+1:
            li.append(i+1)
            U += 1
            if U == 2:
                break
    dic.update({str(n+1): li[1]})

K = [v[0] for v in sorted(dic.items(), key=lambda x:x[1])] 
print(' '.join(K))

