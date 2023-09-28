#약수를 리스트로 구한 다음에
#리스트(sum) 이용해서 모두 더하면 되지 않을까

while True:
    n = int(input())
    if n == -1: break #기점
    
    li = [1,]
    for i in range(2, n):
        if n % i == 0:
            li.append(i)

    if sum(li) == n:
        print(n, "=", end = ' ')
        for j in range(len(li) - 1):
            print(li[j], "+", end = ' ')
        print(li[-1])
    else:
        print("{} is NOT perfect.".format(n))