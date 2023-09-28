#m, n 모두 포함되어야 한다.
m = int(input())
n = int(input())
sum = 0
smallest = 10000 #10000이하의 자연수이므로 기준
for i in range(m, n+1):
    if i == 1: continue
    for j in range(2, i):
        if i % j == 0: break
    else: #소수라면
        sum = sum + i
        if i < smallest: smallest = i

if sum == 0: print(-1) #소수가 없다면
else:
    print(sum)
    print(smallest)
    