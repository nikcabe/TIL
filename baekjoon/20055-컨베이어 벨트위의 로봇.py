from collections import deque

N, K = map(int, input().split())
# 내구도 저장
belt = deque(map(int, input().split()))
# 로봇의 위치
robot = deque([0]*N)

turn = 0
while True:
    turn += 1

    # Step 1: 벨트를 한 칸 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 내리는 위치는 로봇 정차 금지

    # Step 2: 로봇을 한 칸 이동할 수 있다면 이동
    for i in range(N-2, -1, -1):  # 뒤에서부터 차례로 이동
        if robot[i] and not robot[i+1] and belt[i+1]:  # 다음 칸이 비었고 내구도가 있으면 이동
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1  # 내구도 감소
            if belt[i+1] == 0:
                K -= 1  # 내구도 0이 된 칸 계산
    robot[-1] = 0  # 내리는 위치의 로봇 제거

    # Step 3: 로봇을 올리자
    if belt[0] > 0:  # 올리는 위치 내구도가 1 이상이면 가능
        robot[0] = 1
        belt[0] -= 1  # 내구도 감소
        if belt[0] == 0:
            K -= 1  # 내구도 0 처리

    # Step 4: 내구도가 0인 칸이 K개 이상인지 확인
    if K <= 0:  # 종료 조건 충족
        print(turn)
        break
