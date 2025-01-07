import heapq

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve():
    problem_num = 1
    while True:
        # 입력받기
        data = input().split()
        N = int(data[0])
        if N == 0:
            break

        cave = []
        index = 1
        for _ in range(N):
            cave.append(list(map(int, data[index:index + N])))
            index += N

        # 최소 비용 저장 배열
        INF = int(1e9)
        dist = [[INF] * N for _ in range(N)]

        # 우선순위 큐 초기화
        pq = []
        heapq.heappush(pq, (cave[0][0], 0, 0))
        dist[0][0] = cave[0][0]

        # 다익스트라 알고리즘
        while pq:
            current_cost, x, y = heapq.heappop(pq)

            # 이미 처리된 경우
            if current_cost > dist[x][y]:
                continue

            # 인접 노드 탐색
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    next_cost = current_cost + cave[nx][ny]
                    if next_cost < dist[nx][ny]:
                        dist[nx][ny] = next_cost
                        heapq.heappush(pq, (next_cost, nx, ny))

        # 결과 출력
        print(f"Problem {problem_num}: {dist[N-1][N-1]}")
        problem_num += 1

# 실행
solve()