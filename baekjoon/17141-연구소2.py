from itertools import combinations
from collections import deque

n, m = map(int,input().split())
board = []
virus = []
# 바이러스 넣을 수 있는 곳 전부 확인
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i,j))
def bfs(virus):
    # 바이러스가 가장 오래 걸린 곳의 시간을 파악 하기 위해 max_time을 사용함
    max_time = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    # 방문 했는지 여부를 파악하기 위해 -1의 NxN 배열을 만듬
    visited = [[-1] * n for _ in range(n)]
    # 조합에서 뽑힌 바이러스의 자리에서 시작하기 때문에 방문표시 해줌
    for v in virus:
        visited[v[0]][v[1]] = 0
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 방문 한적 없고 벽이 아닌 곳일 경우 q에 추가
                if visited[nx][ny] == -1 and board[nx][ny] != 1:
                    q.append((nx, ny))
                    # 1번 갈때 1초 증가하기 때문에 +1을 해줌
                    visited[nx][ny] = visited[x][y] + 1
                    max_time = max(max_time, visited[nx][ny])
    # 다 돌렸으나 감염시키지 못했거나 방문하지 않았다면 원래 값을 돌려줌
    for i in range(n):
        for j in range(n):
            if (board[i][j] == 0 or board[i][j] == 2) and visited[i][j] == -1:
                return 1e9

    return max_time
ans = 1e9
# combinations를 사용하요 조합을 사용
for comb in combinations(virus,m):
    # bfs돌린 것을 하나하나 비교해줌
    ans = min(bfs(comb),ans)
# 값이 변화했다면
if ans != 1e9:
    print(ans)
# 값이 그대로라면
else:
    print(-1)