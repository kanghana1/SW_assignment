#직사각형을 좌표처럼 생각하고 상하좌우로 자른다. 
#어디쪽에 더 가까운지 무한 if 해서 거리를 구한다. 
x, y, w, h = map(int, input().split())
if (w / 2) < x:
    if (h / 2) < y:
        if (w - x) > (h - y): print(h - y)
        else: print(w - x)
    else:
        if (w - x) > y: print(y)
        else: print(w-x)
else:
    if (h / 2) < y:
        if x > (h - y): print(h - y)
        else: print(x)
    else:
        if x > y: print(y)
        else: print(x)
