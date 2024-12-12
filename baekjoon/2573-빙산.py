from collections import deque

def bfs(a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[a, b]])
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] != 0:  # 빙산이 존재하면
                    visited[nx][ny] = True  # 방문 처리
                    queue.append([nx, ny])  # 큐에 추가
                else:  # 바닷물인 경우
                    cnt[x][y] += 1  # 현재 위치의 바닷물 접촉 카운트 증가
    return 1  # 탐색 완료 시 1 반환

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

year = 0

# 빙산이 모두 녹을 때까지 반복
while True:
    answer = []  # 빙산 덩어리 개수를 저장
    visited = [[False] * m for _ in range(n)]  # 방문 상태 초기화
    cnt = [[0] * m for _ in range(n)]  # 바닷물과 접촉한 빙산 카운트 초기화

    # 빙산주변 파악!
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:  # 아직 방문하지 않은 빙산 발견 시
                answer.append(bfs(i, j))  # BFS 탐색 수행 및 결과 저장

    # 빙산 높이 감소!
    for i in range(n):
        for j in range(m):
            graph[i][j] -= cnt[i][j]  # 빙산 높이 감소
            if graph[i][j] < 0:  # 높이가 음수가 되면 0으로 설정
                graph[i][j] = 0

    if len(answer) == 0 or len(answer) >= 2:  # 빙산이 없거나 두 덩어리 이상으로 분리되면 종료
        break

    year += 1  # 1년 경과

print(year) if len(answer) >= 2 else print(0)  # 결과 출력
