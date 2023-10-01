x_li = []
y_li = []

for i in range(3):
    x, y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)

fin = []
for i in range(3):
    if x_li.count(x_li[i]) == 1:
        fin.append(x_li[i])
        break

for j in range(3):
    if y_li.count(y_li[j]) == 1:
        fin.append(y_li[j])
        break

print(fin[0], fin[1])