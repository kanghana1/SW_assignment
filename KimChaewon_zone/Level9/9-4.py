#소수는 본인과 1제외 하고 약수가 있나없나 구하면 되겠다
#첫 줄의 n는 for문의 기준

n = int(input())
li = map(int, input().split())
count = 0 #소수의 개수 
for elem in li: #리스트의 요소들 / 소수로 비교할 수
    if elem == 1: continue #1이 조건에 맞지 않아서 바로 else 문으로 넘어가니까
    for j in range(2, elem):
        if elem % j == 0: 
            break
    else:
        count += 1

print(count)