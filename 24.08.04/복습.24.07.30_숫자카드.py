T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num_list = [0] * 10
    arr = list(map(int,input()))
    for k in arr:
        num_list[k] +=1
    max_v = 0
    for i in range(10):
        if max_v < num_list[i]:
            max_v = num_list[i]
            max_idx = i
    print(f'#{tc} {max_idx} {max_v}')
