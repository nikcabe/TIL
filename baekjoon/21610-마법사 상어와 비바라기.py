# 1. 구름 이동과 비로 인한 수위 증가
# 2. 물복사
# 3. 구름 생성

N,M = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(N)]
di = [0,0,-1,-1,-1,0,1,1,1]
dj = [0,-1,-1,0,1,1,1,0,-1]
clde = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

for _ in range(M):
    D,S = list(map(int,input().split()))

    # 1. 구름 이동과 비로 인한 수위 증가
    clde1 = []
    for ci,cj in clde:
        ni,nj = (ci+di[D]*S) % N, (cj+dj[D]*S) % N
        arr[ni][nj] += 1
        clde1.append((ni,nj))


    # 2. 물복사
    for ci,cj in clde1:
        for dii, djj in ((-1,1),(-1,-1),(1,-1),(1,1)):
            ni,nj = ci+dii, cj+djj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                arr[ci][cj] += 1

    # 3. 구름 생성
    clde = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i,j) not in clde1:
                arr[i][j] -= 2
                clde.append((i,j))

ans = 0
for lst in arr:
    ans += sum(lst)
print(ans)