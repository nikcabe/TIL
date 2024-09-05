from collections import deque

def bfs():
    # queue가 존재할때 까지 반복
    while queue:
        # popleft() 메소드를 호출하여 queue의 왼쪽 끝 값을 꺼냄
        x,y = queue.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            # 새로운 좌표가 배열 범위안에 있고 방문하지 않은 위치기 0일 경우
            if 0<= a <N and 0 <= b < M and arr[a][b] == 0:
                # 새 좌표를 큐에 추가
                queue.append([a,b])
                # 새로운 좌표의 값은 현재 좌표 +1을 설정하여, 거리 또는 탐색 깊이를 기록한다.
                arr[a][b] = arr[x][y] + 1

M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i,j])

dx = [0,1,0,-1]
dy = [1,0,-1,0]
bfs()
result = 0
# 배열을 순회해서 탐색 결과를 확인함
for i in arr:
    for j in i:
        if j == 0:      # 만약 0이 남아있다면 모든 노드를 방문하지 못한 경우
            print(-1)
            exit()      # 프로그램 종료
    # max(i)로 행의 최대 값과 result를 비교해서 가장 큰 값을 result에 넣는다.
    result = max(result, max(i))
# 시작점이 1이기 때문에 일수는 -1을 해줘야 한다.
print(result-1)