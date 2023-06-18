#提出したコードの修正
n = int(input())
s = input()
k = [s[i]*2 for i in range(n)]
print(''.join(k))
