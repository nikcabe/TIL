from collections import deque
def bfs():
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            for l in range(N):
                nx = x+di[4]*l
                ny = y+dj[4]*l
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] ==

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
queue = deque()
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            queue.append([i,j])
for i in range(N):
    for j in range(N):
        for _ in range(3):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                cnt += 1

di = [0,1,0,-1]
dj = [1,0,-1,0]

bfs()