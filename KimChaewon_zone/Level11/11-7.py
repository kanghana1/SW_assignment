a, b = map(int, input().split())
c = int(input())
n = int(input())

#무조건 n만 보면 안되는 이유는 n 이후에 혹시라도 함수끼리 만나는 점이 생길 수 있기 때문 
for i in range(n, 101):
    if a * i + b <= c * i:
        continue
    else:
        print(0)
        break
else:
    print(1)