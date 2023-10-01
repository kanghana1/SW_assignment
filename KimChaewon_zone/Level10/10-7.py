while True:

    li = list(map(int, input().split()))
    a = max(li)
    li.remove(max(li)) #remove는 지우고 싶은 요소의 값을 인자로 전달. 중복되면 하나의 값만 지움(맨 앞에 있는)
    b = li[0]
    c = li[1]
    if a == b == c == 0: break
    if a < (b + c):
        if a == b == c: print("Equilateral")
        elif a == b or b == c or c == a: print("Isosceles")
        else: print("Scalene")
    else:
        print("Invalid")