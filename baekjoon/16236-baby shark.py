from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

# 시작 위치 찾기
def find_shark_position():
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                return i, j

# 먹을 수 있는 물고기의 리스트 정렬 기준 함수
def sort_key(fish):
    return (fish[0], fish[1], fish[2])

# BFS
def bfs(x, y, size):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x, y]])
    # 먹을 수 있는 물고기들의 리스트
    cand = []
    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            dx, dy = i + di[k], j + dj[k]
            if 0 <= dx < N and 0 <= dy < N and visited[dx][dy] == 0:
                if space[dx][dy] == 0 or space[dx][dy] == size:  # 빈칸이거나 상어와 같은 크기의 물고기
                    visited[dx][dy] = visited[i][j] + 1
                    queue.append([dx, dy])
                elif 0 < space[dx][dy] < size:  # 상어보다 작은 물고기
                    visited[dx][dy] = visited[i][j] + 1
                    cand.append((visited[dx][dy] - 1, dx, dy))
                    queue.append([dx, dy])

    return sorted(cand, key=sort_key)

# 상어의 위치를 찾는다
i, j = find_shark_position()

# 상어의 크기와 먹은 물고기 수
size = [2, 0]
cnt = 0

# 상어가 더 이상 먹을 물고기가 없을 때까지 반복
while True:
    space[i][j] = 0  # 상어가 있던 자리는 빈칸으로 만듦
    cand = deque(bfs(i, j, size[0]))  # 먹을 물고기 찾기

    if not cand:
        break

    # 가장 가까운 물고기로 이동
    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1  # 물고기 먹음

    # 상어의 크기만큼 물고기를 먹으면 크기 증가
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    # 상어를 새로운 위치로 이동
    i, j = xx, yy

# 총 이동한 거리 출력
print(cnt)
