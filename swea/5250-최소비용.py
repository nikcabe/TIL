from collections import deque
def dijkstra(x,y):
    q = deque([(x,y)])
    visited[x][y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny <n:
                wei = 0
                if arr[nx][ny] > arr[x][y]:
                    wei += arr[nx][ny] - arr[x][y]
                if visited[nx][ny] > visited[x][y]+wei+ 1:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + wei + 1


dx = [0,1,0,-1]
dy = [1,0,-1,0]
T = int(input())

for tc in range(1,1+T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [[1e9 for _ in range(n)]for _ in range(n)]
    dijkstra(0,0)
    print(f'#{tc} {visited[n-1][n-1]}')