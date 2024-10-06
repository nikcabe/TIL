# 시작점은 언제나 하나!
def X_find(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                return i,j

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    Q = int(input())
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    # 결과를 한줄에 넣기 위해 리스트 생성
    result = []

    for w in range(Q):
        # 시작점을 x,y로 지정
        x, y = X_find(N)
        k = 0
        c, direction = list(input().split())
        for z in range(int(c)):
            # L일경우 k-1을 하여 왼쪽으로 회전
            if direction[z] == 'L':
                k = (k - 1) % 4
            # R일경우 k+1을 하여 오른쪽으로 회전
            elif direction[z] == 'R':
                k = (k + 1) % 4
            # 양쪽 다 아닐 경우 직진하기!
            else:
                ni = x+di[k]
                nj = y+dj[k]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 'T':
                    x,y = ni,nj
        # 목적지를 확인하는 문제기 때문에 다 돌린 후 확인
        if arr[x][y] == 'Y':
            result.append(1)
        else:
            result.append(0)
    print(f"#{tc}",*result)