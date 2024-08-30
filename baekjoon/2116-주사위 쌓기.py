N = int(input())
dic = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
dice = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(6):
    sum_v = 0
    tmp = [1, 2, 3, 4, 5, 6]
    tmp.remove(dice[0][i])
    '''
    dic[i] = 인덱스 첫줄의 a의 반대 인덱스
    dice[0][dic[i]] = 입력 받은 주사위에서 반대 인덱스의 값을 찾아내는 방법
    '''
    step = dice[0][dic[i]]
    tmp.remove(step)
    sum_v += max(tmp)

    for j in range(1, N):
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.remove(step)
        step = dice[j][dic[dice[j].index(step)]]
        tmp.remove(step)
        sum_v += max(tmp)
    ans = max(ans, sum_v)
print(ans)