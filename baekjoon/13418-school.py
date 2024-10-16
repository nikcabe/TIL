import heapq
import sys

input = sys.stdin.readline

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])  # 경로 압축
    return parents[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        # 더 작은 루트 노드에 합친다.
        if root_x < root_y:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y

# V: 정점(건물) 수, E: 간선(도로) 수 입력
V, E = map(int, input().split())
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))  # (출발, 도착, 가중치) 형태로 저장

# 가중치 기준으로 오름차순 정렬
edges.sort(key=lambda x: x[2])

# 대표원소 배열 초기화
parents = [i for i in range(V + 1)]

# MST의 간선 수 N = 정점 수 - 1
cnt = 0     # 선택한 edge의 수 (N - 1 가 되면 신장 트리 완성)
total_min = 0   # 최소 피로도의 합
total_max = 0   # 최대 피로도의 합

# 최소 피로도 (오르막길이 적은 경로)
for u, v, w in edges:
    if find_set(u) != find_set(v):  # 싸이클이 없다면
        if w == 0:  # 오르막길
            total_min += 1
        union(u, v)
        cnt += 1
        if cnt == V:  # MST 구성이 끝나면
            break

# 최대 피로도 (오르막길이 많은 경로)
cnt = 0  # 리셋
parents = [i for i in range(V + 1)]  # 대표원소 배열 초기화
for u, v, w in reversed(edges):  # 가중치가 높은 것부터 시작
    if find_set(u) != find_set(v):  # 싸이클이 없다면
        if w == 0:  # 오르막길
            total_max += 1
        union(u, v)
        cnt += 1
        if cnt == V:  # MST 구성이 끝나면
            break

# 최악 피로도와 최적 피로도의 차이 계산
difference = (total_max ** 2) - (total_min ** 2)
print(f'최악 피로도와 최적 피로도의 차이 = {difference}')
