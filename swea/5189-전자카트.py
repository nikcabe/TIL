def f(i,j,sum_value):
    # 기저조건
    if i == j:
        return
    elif sum_value > min_value:
        return

T = int(input())

for tc in range(1,1+T):
    n = int(input())
    arr = [list(map(int,input().split()))]
    min_value = 1001
    f(0,0,min_value)