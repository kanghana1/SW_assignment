n, m = map(int, input().split())
N = 0
M = 0
li = []
for _ in range(n):
    string = input()
    li.append(string)
min = 0
while True:  
    if N + 8 > n: break
    for j in range(N, N+8):
        count = 0
        if M + 8 > m: break
        for i in range(M, M + 8):
            if li[N][M] == "B":
                if i % 2 == 0:
                    if j % 2 == 1:
                        if li[i][j] == "B":count += 1
                    else:
                        if li[i][j] == "W": count += 1
                else:
                    if j % 2 == 1:
                        if li[i][j] == "W": count += 1
                    else:
                        if li[i][j] == "B": count += 1
            else:
                if i % 2 == 0:
                    if j % 2 == 1:
                        if li[i][j] == "W": count += 1
                    else:
                        if li[i][j] == "B": count += 1
                else:
                    if j % 2 == 0:
                        if li[i][j] == "W": count += 1
                    else: 
                        if li[i][j] == "B": count += 1
        
        if count < min: min = count
        M += 1
    N += 1

print(min)

