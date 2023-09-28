#첫번째 변수가 기준이 됨 
#n(for문의 기준), k(if문 기준)

n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    if n % i == 0: count += 1
    if count == k:
        print(i)
        break
else: #만일 for문이 다 수행되었다면, --> 조건에 맞는 수가 없었다면 
    print(0)