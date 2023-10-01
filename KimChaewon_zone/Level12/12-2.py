min = 1000000
n = int(input())
for i in range(n - 1, 0, -1):
    sum = 0
    x = i
    sum = sum + x

    while True:
        sum = sum + (x % 10)
        x = x // 10
        if x // 10 == 0:
            sum += x
            break
    
    if sum == n and i < min:
        min = i 

if min == 1000000: print(0)
else: print(min)