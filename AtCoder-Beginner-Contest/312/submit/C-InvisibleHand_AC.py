def cp(sell, buy, X):
    sc = sum(1 for price in sell if price <= X)
    bc = sum(1 for price in buy if price >= X)
    return sc, bc
 
def price(sell, buy):
    low = min(sell + buy)  
    high = max(sell + buy)  
 
    while low <= high:
        mid = (low + high) // 2
        sc, bc = cp(sell, buy, mid)
 
        if sc >= bc:high = mid - 1
        else:low = mid + 1
    return low
 
N, M = map(int, input().split())
sell = list(map(int, input().split()))
buy = list(map(int, input().split()))
 
sell.sort()
buy.sort()
res = price(sell, buy)
print(res)
