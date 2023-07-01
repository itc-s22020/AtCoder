n=int(input())
s=[input() for i in range(n)]
ans="No"

for i in range(n):
    for j in range(n):
        if i!=j:
            t=s[i]+s[j]
            flag=True
            for k in range(len(t)):
                if t[k]!=t[-k-1]:
                    flag=False
            if flag:
                ans="Yes"

print(ans)

