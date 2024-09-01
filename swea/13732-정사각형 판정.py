def inspect():
    for q in range(n):
        cnt = 0
        for r in range(n):
            if arr[r][q] == '#':
                cnt += 1
            if cnt > b:
                return 'no'
    return 'yes'


T = int(input())

for tc in range(1, 1+T):
    found = False
    n = int(input())
    arr = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                x,y = i, j
                found = True
                break
        if found:
            break
    b = arr[x].count('#')
    if b == 1:
        result = inspect()
    else:
        if arr[x][y:y+b] == '#'* b:
            for k in range(1,b):
                if arr[x+k][y:y+b] != '#'* b:
                    result = 'no'
                    break
                else:
                    result = inspect()
        else:
            result = 'no'

    print(f'#{tc} {result}')
