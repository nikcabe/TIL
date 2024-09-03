T = int(input())

for tc in range(1,1+T):
    n = int(input())
    cnt = 0
    empty = [[0]*10 for _ in range(10)]
    for _ in range(n):
        a1, b1, a2, b2, c = list(map(int, input().split()))
        for i in range(a1,a2+1):
            for j in range(b1,b2+1):
                empty[i][j] += c
                if empty[i][j] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')