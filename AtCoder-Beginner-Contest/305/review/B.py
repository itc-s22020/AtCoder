#提出したコードの修正
s = {"A": 0,"B": 1,"C": 2,"D": 3,"E": 4,"F": 5,"G": 6}
l = [0,3,1,4,1,5,9]
x = 0
for i in range(s[a], s[b]+1):
    if i == s[a]:x -= l[i]
    x += l[i]
print(x)
