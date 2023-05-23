n = int(input("Put the count of coins: "))
count = 0
AxCoins = 0
for i in range(n):
    x = int(input("Put number 0 or 1: "))
    if x == 0:
        count += 1
        AxCoins = count
            
print(AxCoins)