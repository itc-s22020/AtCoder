import itertools

s = int(input())
l = [input() for _ in range(s)]

def c(s1,s2):
    defailtTxt = s1 + s2
    reverseTxt = defailtTxt[::-1]
    return (defailtTxt==reverseTxt) 

for i,s1 in enumerate(l):
    k = []
    k.append(l[:i])
    k.append(l[i+1:])
    for s2 in list(itertools.chain.from_iterable(k)):
        if (c(s1, s2)):
            print("Yes")
            exit()
print("No")
