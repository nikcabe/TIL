from collections import deque

# BFS 함수: 그룹 내 노드들이 연결되어 있는지 확인하고, 그룹의 인구 합을 계산
def bfs(g):
    q = deque()  # 큐를 사용하여 너비 우선 탐색(BFS)을 수행
    check = [False for _ in range(n)]  # 방문 여부를 기록하는 배열, 초기값은 모두 False
    q.append(g[0])  # 그룹의 첫 번째 노드를 큐에 추가
    check[g[0]] = True  # 첫 번째 노드를 방문한 것으로 표시
    cnt, answer = 1, 0  # cnt: 방문한 노드의 수, answer: 그룹의 인구 합을 저장하는 변수

    while q:
        temp = q.popleft()  # 큐에서 노드를 꺼냄
        answer += people[temp]  # 꺼낸 노드의 인구 수를 answer에 더함
        for i in board[temp]:  # 현재 노드(temp)의 인접 노드들에 대해
            if i in g and not check[i]:  # 인접 노드(i)가 그룹 g에 포함되고 방문하지 않았으면
                check[i] = True  # 인접 노드를 방문한 것으로 표시
                cnt += 1  # 방문한 노드 수 증가
                q.append(i)  # 인접 노드를 큐에 추가

    # 그룹의 모든 노드를 방문했는지 확인
    if cnt == len(g):
        return answer  # 모든 노드를 방문했으면, 그룹의 인구 합을 반환
    else:
        return False  # 그렇지 않으면 False 반환 (즉, 연결되지 않은 그룹)

# DFS 함수: 가능한 모든 그룹 조합을 탐색하여 최적의 인구 차이를 찾음
def dfs(cnt, x, end):
    global min_value  # 최솟값을 저장할 전역 변수

    if cnt == end:  # 목표 그룹 크기(end)에 도달했으면
        g1, g2 = deque(), deque()  # 두 그룹을 저장할 덱

        # 모든 노드를 순회하여 방문된 노드는 그룹 1(g1)에, 방문되지 않은 노드는 그룹 2(g2)에 추가
        for i in range(n):
            if visited[i]:
                g1.append(i)
            else:
                g2.append(i)
        ans1 = bfs(g1)  # 그룹 1의 인구 합 계산

        if not ans1:  # 그룹 1이 연결되지 않으면
            return  # 종료

        ans2 = bfs(g2)  # 그룹 2의 인구 합 계산

        if not ans2:  # 그룹 2가 연결되지 않으면
            return  # 종료

        # 두 그룹의 인구 차이를 계산하고 최솟값 업데이트
        min_value = min(min_value, abs(ans1 - ans2))
        return

    # DFS를 사용하여 가능한 모든 조합을 탐색
    for i in range(x, n):
        if visited[i]:  # 이미 방문한 노드는 건너뜀
            continue
        visited[i] = True  # 현재 노드를 방문한 것으로 표시
        dfs(cnt + 1, i, end)  # 다음 노드로 DFS 수행

        # 백트래킹: 현재 노드를 다시 미방문 상태로 설정
        visited[i] = False

# 입력을 읽어들임
n = int(input())  # 노드의 개수 입력
people = list(map(int, input().split()))  # 각 노드의 인구 수 입력

# 인접 리스트를 초기화
board = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))  # 각 노드의 인접 노드 입력
    for j in x[1:]:  # 첫 번째 원소는 노드의 개수, 나머지는 인접 노드
        board[i].append(j - 1)  # 1-based 인덱스를 0-based로 변환하여 저장

min_value = 1e9  # 최소 차이를 저장할 변수, 초기값은 무한대

# 그룹의 크기를 1부터 n//2까지 탐색
for i in range(1, n // 2 + 1):
    visited = [False for _ in range(n)]  # 방문 여부 배열 초기화
    dfs(0, 0, i)  # DFS를 시작하여 모든 조합을 탐색

# 결과 출력
if min_value == 1e9:  # 가능한 그룹 조합이 없는 경우
    print(-1)  # -1 출력
else:
    print(min_value)  # 최소 인구 차이 출력
