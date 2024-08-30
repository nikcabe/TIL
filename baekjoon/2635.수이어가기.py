N = int(input())
# 답이 들어갈 리스트 생성
ans = []

for i in range(1, 1+N):
    '''
    first와 second를 두 지점으로 삼는다.
    '''
    first = N
    second = i
    # 규칙에 따른 수들을 넣는 리스트를 생성한다. first와 second는 리스트의 첫번째와 두번째 수 이기 때문에 미리 넣어둔다.
    tmp = [first, second]
    while True:
        # 첫번쨰 정수에서 두번쨰 정수를 빼서 세번째에 해당하는 정수를 만들어 둔다.
        next_num = first - second
        '''
        세번째 정수가 0보다 크다면 리스트에 해당 숫자를 입력한다.
        두번째 정수를 첫번째 변수로 옮기고 세번쨰 변수가 두번째로 옮겨진다.
        '''
        if next_num >= 0:
            tmp.append(next_num)
            first = second
            second = next_num
        # 답 리스트의 길이와 규칙 리스트의 길이를 비교해서 규칙 리스트가 더 크다면 ans에 tmp를 삽입한다.
        else:
            if len(tmp) > len(ans):
                ans = tmp
            break
print(len(ans))
print(*ans)