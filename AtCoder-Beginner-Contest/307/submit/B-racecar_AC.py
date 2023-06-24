#[AC] 466Byte 100ms 9180KB Python3
import itertools

s = int(input())
l = [input() for _ in range(s)]

def c(s1,s2):
    ss = s1 + s2
    r = ""
    for i in range(len(ss)-1,-1,-1):
        r+=ss[i]
    if(r==ss):
        return True
    else:
        return False

for i,s1 in enumerate(l):
    k = []
    k.append(l[:i])
    k.append(l[i+1:])
    for s2 in list(itertools.chain.from_iterable(k)):
        if (c(s1, s2)):
            print("Yes")
            exit()
print("No")
