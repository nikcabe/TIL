def find_set(i):
    while i != rep[i]:
        i = rep[i]
    return i
def union(i,j):
    rep[find_set(j)] = find_set(i)

T = int(input())

for tc in range(1,1+T):
    V,E = map(int,input().split())  # 0번부터 v번까지 노드와 E개의 간선
    edge = [list(map(int,input().split())) for _ in range(E)]

    rep = [i for i in range(V+1)]

    edge.sort(key = lambda x:x[2])

    cnt = 0
    ans = 0
    for n1,n2,w in edge:
        if find_set(n1) != find_set(n2):
            union(n1,n2)
            cnt+=1
            ans+=w
        if cnt == V:
            break
    print(f'#{tc} {ans}')