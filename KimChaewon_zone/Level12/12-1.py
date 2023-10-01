n, m = map(int, input().split())

li = list(map(int, input().split()))
app = 1000000000
for i in range(n):
    a = li[i]
    for j in range(i + 1, n):
        b = li[j]
        for k in range(j + 1, n):
            c = li[k]
            sum = a + b + c
            if sum > m: continue
            else:
                if app > m - sum:
                    app = m - sum
                else: continue

print(m - app)