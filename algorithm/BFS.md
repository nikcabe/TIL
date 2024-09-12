## 그래프를 탐색하는 방법에는 두 가지가 있음

- 깊이 우선 탐색
- 너비 우선 탐색

## 너비우선탐색은 탐색 시작점의인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

## 인접한 정점들에 대해 탐색을 한 후, 차례에 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함

## BFS예시 그래프

https://github.com/user-attachments/assets/759fbdd5-cd66-4dae-b25f-c2238bfbc81d

## 입력 파라미터: 그래프 G와 탐색 시작점 v

```python
		def BFS(G,v):   # 그래프 G, 탐색 시작점 v 
			**visited = [0]*(n+1)    # n: 정점의 개수, 방문 기록(준비)
			queue = []             # 큐 생성                  (준비)
			queue.append(v)        # 시작점 v를 큐에 삽입     (준비)**
			while queue:           # 큐가 비어있지 않은 경우
				t = queue.pop(0)     # 큐의 첫번째 원소 반환 <- 방문할 노드
				if not visited[t]    # 방문되지 않은 곳이라면
					visited[t] = True  # 방문한 것으로 표시
					visit(t)           # 정점 t에서 한 일
					for i in G[t]:     # t와 연결된 모든 정점에 대해
						 if not visited[i]:    #방문되지 않은 곳이라면
							 queue.append(i)     # 큐에 넣기
```

```python
		def BFS(G,v):   # 그래프 G, 탐색 시작점 v 
			**visited = [0]*(n+1)    # n: 정점의 개수, 방문 기록(준비)
			queue = []             # 큐 생성                  (준비)
			queue.append(v)        # 시작점 v를 큐에 삽입     (준비)
			visitd[v] = 1**
			while queue:           # 큐가 비어있지 않은 경우
				t = queue.pop(0)     # 큐의 첫번째 원소 반환 <- 방문할 노드
				visit(t)           # 정점 t에서 한 일
				for i in G[t]:     # t와 연결된 모든 정점에 대해
					if not visited[i]:    #방문되지 않은 곳이라면
						queue.append(i)     # 큐에 넣기
						visited[i] = visited[t]+1 # N으로 부터 1만큼 이동
```