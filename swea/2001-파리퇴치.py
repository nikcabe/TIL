T = int(input())

for tc in range(1,1+T):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_num = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_num = 0
            for k in range(m):
                for l in range(m):
                    sum_num += arr[i+k][j+l]
            if max_num < sum_num:
                max_num = sum_num
    print(max_num)