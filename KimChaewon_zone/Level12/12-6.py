n = int(input())
sum = 0
a = n // 5
while a != 0:
    if (n - (a * 5)) % 3 == 0 :
        sum = a + (n - (a*5)) // 3
        break
    else:
        a -= 1

if sum == 0:
    if n % 3 == 0: sum = n // 3
    else: sum = -1

print(sum)