def bfs():
    global cnt  # 전역 변수 cnt

    # set을 사용하여 중복된 상태를 제거
    queue = set([(0, 0, graph[0][0])])

    while queue:
        x, y, z = queue.pop()

        # 최대 칸 수를 갱신
        cnt = max(cnt, len(z))

        for i in range(4):
            nx = x + dx[i]  # 이동 후의 x 좌표 계산
            ny = y + dy[i]  # 이동 후의 y 좌표 계산

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in z:
                # 새로운 상태를 큐에 추가
                queue.add((nx, ny, z + graph[nx][ny]))


r, c = map(int, input().split())

graph = [list(map(str, input().strip())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 1

bfs()
print(cnt)
