t = int(input())

for _ in range(t):
    n = int(input())

    number = [input().strip() for _ in range(n)]

    # 이거 안해서 계속 틀림 ㅠㅠ
    number.sort()

    # 일관성 여부를 체크하는 변수
    check = 1

    # 전화번호 목록을 순회, 접두어 관계를 검사
    for i in range(n-1):
        for j in range(i+1, n):
            if number[i] == number[j][:len(number[i])]:
                check = 0
                break

    if check == 0:
        print('NO')
    else:
        print('YES')