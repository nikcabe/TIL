from collections import deque
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

pos = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            pos.append(i)
            pos.append(j)

cnt = 0

def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x, y]])
    cand = []
    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()
        for idx in range(4):
            ii, jj = i + dx[idx], j + dy[idx]
            if 0 <= ii < N and 0 <= jj < N and visited[ii][jj] == 0:
                if space[x][y] > space[ii][jj] and space[ii][jj] != 0:
                    visited[ii][jj] = visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif space[x][y] == space[ii][jj]:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])

                elif space[ii][jj] == 0:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])

    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


i, j = pos

# 아기 상어의 크기와 먹은 물고기 수
size = [2, 0]  # 초기 크기는 2, 먹은 물고기 수는 0

# 계속해서 물고기를 먹을 수 있을 때까지 반복
while True:
    space[i][j] = size[0]  # 현재 위치를 상어의 크기로 설정 (9 -> 상어 크기)
    cand = deque(bfs(i, j))  # 먹을 수 있는 물고기 후보를 BFS로 찾음

    if not cand:  # 후보가 없으면 종료 (먹을 물고기가 없을 때)
        break

    # 가장 가까운 물고기를 선택
    step, xx, yy = cand.popleft()
    cnt += step  # 이동한 거리를 더함
    size[1] += 1  # 먹은 물고기 수를 1 증가

    # 먹은 물고기 수가 상어의 크기와 같아지면 상어 크기 증가
    if size[0] == size[1]:
        size[0] += 1  # 상어 크기 증가
        size[1] = 0  # 먹은 물고기 수 초기화

    space[i][j] = 0  # 원래 상어가 있던 자리는 빈칸으로 만듦
    i, j = xx, yy  # 상어의 위치를 물고기 먹은 위치로 이동

# 총 이동한 거리를 출력
print(cnt)