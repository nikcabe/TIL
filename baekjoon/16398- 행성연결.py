# 서건호

'''
MST 크루스칼 알고리즘

1. 부모 테이블을 만듬
2. 부모 테이블을 자기 자신으로 초기화
3. 간선들을 리스트에 저장
4. 간선들을 오름차순을 정렬
5. 간선을 하나하나 확인한다.
6. 사이클을 확인해서 발생하지 않는다면 집합에 포함

	- 부모노드를 비교
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 부모 테이블을 만듬
parent = [0] * (N+1)
edges = []
# 2. 부모 테이블을 자기 자신으로 초기화
for k in range(1,N+1):
    parent[k] = k

# 부모노드를 찾는 함수
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 노드를 합치는 함수
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 3. 간선들을 리스트에 저장
# 행렬은 Cij가 i=j인 경우를 기준으로 대칭이다. 그러므로 한쪽면만 취한다.
for i in range(0,N):
    for j in range(i+1,N):
        edges.append((arr[i][j],i,j))

# 4. 간선들을 오름차순을 정렬
edges.sort()
result = 0

# 5. 간선을 하나하나 확인한다.
for edge in edges:
    cost, a, b = edge
    # 6. 사이클을 확인해서 발생하지 않는다면 집합에 포함 
    # 부모노드 비교를 통해 사이클인지 여부 확인
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result += cost
print(result)
