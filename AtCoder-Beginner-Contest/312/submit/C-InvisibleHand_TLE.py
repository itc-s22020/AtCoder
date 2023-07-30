def price(sell, buy):
    sell.sort()
    buy.sort()
    
    X = 1
    while True:
        sc = sum(1 for price in sell if price <= X)
        bc = sum(1 for price in buy if price >= X)
        if sc >= bc:
            return X
        X += 1

N,M = input().split()
sell = list(map(int, input().split()))
buy = list(map(int, input().split()))
res = price(sell, buy)
print(res)  

