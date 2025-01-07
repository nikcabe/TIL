from collections import deque

# 상하좌우 이동을 위한 방향 설정
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# BFS로 공기와 접촉하는 치즈를 찾아서 녹임
def bfs(n, m, grid):
    # 공기 영역을 표시하는 배열 (초기 공기는 맨 바깥쪽에 위치)
    visited = [[False] * m for _ in range(n)]
    queue = deque()

    # 가장자리를 공기로 설정 (외부 공기부터 채워나감)
    queue.append((0, 0))  # (0, 0)에서 시작
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        # 상하좌우로 인접한 공간 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 경계를 벗어나지 않고, 아직 방문하지 않은 곳이라면
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 0:  # 빈 공간이면 큐에 추가
                    queue.append((nx, ny))
                elif grid[nx][ny] == 1:  # 치즈가 있으면 녹을 예정
                    grid[nx][ny] = 0  # 치즈 녹이기
    return grid


def count_cheese(n, m, grid):
    return sum(sum(row) for row in grid)  # 남아있는 치즈의 개수


def solve(n, m, grid):
    time = 0
    last_cheese_count = 0

    while True:
        # 남아있는 치즈의 개수
        current_cheese_count = count_cheese(n, m, grid)

        # 더 이상 치즈가 없으면 종료
        if current_cheese_count == 0:
            break

        last_cheese_count = current_cheese_count
        # BFS로 공기와 접촉하는 치즈를 녹이기
        grid = bfs(n, m, grid)
        time += 1

    return time, last_cheese_count


# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
time, last_cheese_count = solve(n, m, grid)
print(time)
print(last_cheese_count)
