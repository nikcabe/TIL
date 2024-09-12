T = int(input())
for tc in range(1,1+T):
    N,E = map(int,input().split())

    edge = [list(map(int,input().split())) for _ in range(E)]

    INF = int(1e9)
    adj = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        adj[i][i] = 0
    for n1,n2,w in edge:
        adj[n1][n2] = w
    D = adj[0][:]
    v = [0]*(N+1)

    for _ in range(N):
        min_v = INF
        t = 0
        for i in range(N+1):
            if v[i] == 0 and min_v > D[i]:
                min_v = D[i]
                t = i
        v[t] = 1
        for w in range(N+1):
            if 0 < adj[t][w]<INF:
                D[w] = min(D[w],D[t] + adj[t][w])
    print(f'#{tc} {D[N]}')