from collections import deque


# 오른쪽으로 기어를 회전시키는 함수
def rotate_right(num, direction):
    # num이 4보다 크면 리턴 (4개의 기어만 있으므로)
    if num > 4:
        return

    # 현재 기어가 회전할 수 있는 상태인지 확인
    if check[num - 1] == False:
        # 현재 기어를 주어진 방향으로 회전
        Gear[num].rotate(direction)
        # 다음 기어(오른쪽)를 확인하고 회전
        rotate_right(num + 1, -direction)


# 왼쪽으로 기어를 회전시키는 함수
def rotate_left(num, direction):
    # num이 1보다 작으면 리턴 (4개의 기어만 있으므로)
    if num < 1:
        return

    # 현재 기어가 회전할 수 있는 상태인지 확인
    if check[num] == False:
        # 현재 기어를 주어진 방향으로 회전
        Gear[num].rotate(direction)
        # 다음 기어(왼쪽)를 확인하고 회전
        rotate_left(num - 1, -direction)


Gear = [0]
# 각 기어의 초기 상태를 입력
for i in range(4):
    # 각 기어의 상태를 deque로 저장
    Gear.append(deque(list(map(int, list(input())))))

for _ in range(int(input())):
    num, direction = map(int, input().split())

    # 현재 기어가 회전할 수 있는 확인하는 리스트 생성
    check = [True, Gear[1][2] == Gear[2][6], Gear[2][2] == Gear[3][6], Gear[3][2] == Gear[4][6], True]

    '''
    rotate(n)의 형태로 사용되며, n은 회전할 방향과 양을 나타냅니다.
    양수일 경우: 오른쪽으로 회전합니다.
    음수일 경우: 왼쪽으로 회전합니다.
    '''
    # 선택한 기어를 주어진 방향으로 회전
    Gear[num].rotate(direction)
    # 오른쪽 기어들을 회전시킴
    rotate_right(num + 1, -direction)
    # 왼쪽 기어들을 회전시킴
    rotate_left(num - 1, -direction)

score = 0
for i in range(4):
    # 각 기어의 12시 방향 값이 1이면 점수 추가
    if Gear[i + 1][0] == 1:
        score += 2 ** i

print(score)