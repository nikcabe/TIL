from collections import deque

def dfs(n,c):
    q = deque([(n,c)])
    visited = set()
    visited.add(n)

    while q:
        if n == M:
            return c
        n,c = q.popleft()
        if n*2 not in visited and 0 <= n*2 <= 1000000:
            q.append((n*2,c+1))
            visited.add(n*2)
        if n+1 not in visited and 0 <= n+1 <= 1000000:
            q.append((n+1,c+1))
            visited.add(n+1)
        if n-1 not in visited and 0 <= n-1 <= 1000000:
            q.append((n-1,c+1))
            visited.add(n-1)
        if n-10 not in visited and 0 <= n-10 <= 1000000:
            q.append((n-10,c+1))
            visited.add(n-10)

T = int(input())

for tc in range(1,1+T):
    n,M = map(int,input().split())
    print(f'#{tc} {dfs(n,0)}')