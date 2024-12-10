n, m = map(int, input().split())  # 청소 구역 크기
r, c, d = map(int, input().split())  # 로봇 청소기의 현재 위치와 방향 지정
arr = [list(map(int, input().split())) for i in range(n)]

move = [(0, -1), (-1, 0), (0, 1), (1, 0)]

ans = 0

while True:
    # 1. 현재 칸 청소 시작
    if not arr[r][c]:  # 청소가 안 된 칸이라면
        arr[r][c] = 2  # 청소
        ans += 1  # 개수 +1

    # 2. 청소할 곳이 있는지 탐색
    for x, y in move:
        dx = r + x
        dy = c + y
        if not arr[dx][dy]:  # 청소 안 한 곳 발견
            break  # 탐색 그만!
    else:
        # 주변이 모두 청소되어 있거나 벽이라면?
        x, y = move[(d - 1) % 4]  # 왼쪽으로 돌려보자!
        dx = r + x
        dy = c + y
        if arr[dx][dy] == 1:  # 벽? 여기 까지..
            break  # 동작 종료
        else:
            r, c = dx, dy  # 후진 성공 계속 진행하자
            continue

    # 3. 왼쪽 방향으로 회전 후 전진
    x, y = move[d]  # 현재 방향 기준으로 이동할 좌표 계산
    dx = r + x
    dy = c + y
    d = (d - 1) % 4  # 방향을 미리 틀어놓음!
    if not arr[dx][dy]:  # 청소할 곳 발견!
        r, c = dx, dy  # 전진
        continue

print(ans)
