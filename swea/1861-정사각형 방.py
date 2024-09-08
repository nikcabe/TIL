di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def DFS(x,y):
    global cnt
    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == arr[x][y] + 1:
                cnt += 1
                DFS(nx, ny)

T = int(input())

for tc in range(1,1+T):
    max_cnt = 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 1
            DFS(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                resultx = i
                resulty = j
            if max_cnt == cnt and arr[i][j] < arr[resultx][resulty]:
                resultx = i
                resulty = j
    print(f'#{tc} {arr[resultx][resulty]} {max_cnt}')