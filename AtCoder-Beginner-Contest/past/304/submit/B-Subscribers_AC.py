num = input()
if int(num) <= 10**3-1:
    print(num)
for i in range(3,9):
    if 10**i <= int(num) <= (10**(i+1)-1):
        print(f'{num[0:-(i-2)]}', end="")
        print("0"*(i-2))