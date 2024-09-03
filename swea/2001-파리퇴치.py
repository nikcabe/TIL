T = int(input())

for tc in range(1,1+T):
    n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # 가장 큰 값 설정
    max_n = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_m = 0
            for k in range(m):
                for l in range(m):
                    sum_m += arr[i+k][j+l]
            if max_n < sum_m:
                max_n = sum_m
    print(max_n)