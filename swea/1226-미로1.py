def start_point():
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                return (i,j)

def dfs():
    while stack:
        x, y = stack.pop()
        for k in range(4):
            dx = x+di[k]
            dy = y+dj[k]
            if 0<= dx <16 and 0 <= dy < 16 and arr[dx][dy] != '1':
                if arr[dx][dy] == '3':
                    return 1
                else:
                    arr[dx][dy] = '1'
                    stack.append((dx, dy))

for tc in range(10):
    T = int(input())
    arr = [list(input()) for _ in range(16)]
    # 시작지점을 찾음
    stack = [start_point()]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    if dfs() == 1:
        print(f'#{T}',1)
    else:
        print(f'#{T}',0)