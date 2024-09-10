di = [0,1,0]
dj = [1,0,-1]

def dfs(arr,x,y):
    global cnt
    print(arr[x][y])
    if arr[x][y] == 1:
        cnt += 1
        return
    else:
        for k in range(3):
            for l in range(arr[x][y]-1):
                nx = i+di[k]*l
                ny = i+dj[k]*l
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] != 1:
                        cnt += arr[nx][ny]
                        dfs(arr, nx, ny)


T = int(input())
for tc in range(1,1+T):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    max_time = 0
    cnt = 0
    for j in range(N):
        for i in range(H):
            if arr[i][j] != 0:
                dfs(arr,i, j)
                break