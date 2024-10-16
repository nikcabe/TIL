from collections import deque

N, L, R = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(N)]
q = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q.append((x, y))
    # 연합 국가들을 저장할 리스트
    union = []
    union.append((x, y))
    while q:
        a,b = q.popleft()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if nx<0 or ny <0 or nx >= N or ny >= N or visited[nx][ny] == 1:
                continue
            # 인구가 L이상 R이하인 경우에만 연합으로 포함
            if R >= abs(arr[a][b]-arr[nx][ny]) >= L:
                visited[nx][ny] = 1
                q.append((nx, ny))
                union.append((nx, ny))
    # 연합에 속한 나라가 1개 이하이면 연합 실패
    if len(union) <= 1:
        return 0
    # 연합 국가들의 인구합산 후 평균값을 계산
    result = sum(arr[x][y] for x,y in union) // len(union)
    for x,y in union:
        arr[x][y] = result
    return 1
day = 0
while 1:
    stop = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                # 이동 발생 여부 기록
                stop += bfs(i,j)
    # 이동이 없다면 종료
    if stop == 0:
        break
    day += 1
print(day)