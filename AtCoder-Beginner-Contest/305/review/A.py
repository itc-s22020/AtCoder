#提出したコードの修正
a=int(input())
b=a//5
c=b*5
print((c,c+5)[a%5>2])

#四捨五入
a=int(input())
print(round(a/5)*5)
