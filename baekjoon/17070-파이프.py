# 서건호

# dp[0][r][c]: (r, c) 위치에 가로 파이프가 놓인 경우의 수
# dp[1][r][c]: (r, c) 위치에 대각선 파이프가 놓인 경우의 수
# dp[2][r][c]: (r, c) 위치에 세로 파이프가 놓인 경우의 수

def solution():
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

    # 시작 위치 (0, 0)에서 (0, 1)까지 가로 파이프를 놓음
    dp[0][0][1] = 1

    # 첫 번째 행의 dp 값 채움
    # 가로 파이프는 현재 셀과 이전 셀(왼쪽)이 모두 0이어야 가능
    for i in range(2, N):
        if board[0][i] == 0:  # 현재 셀이 비어있는지 확인
            # 가로 파이프 옮김
            dp[0][0][i] = dp[0][0][i - 1]

    for r in range(1, N):
        for c in range(1, N):
            # 대각선 파이프는 현재 셀과 왼쪽 셀, 위쪽 셀이 모두 0이어야 놓을 수 있음
            # 그림 참고
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                # 현재 위치로 올 수 있는 값은 위쪽, 대각선, 세로 파이프에서 오는 경우의 수의 합산
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

            if board[r][c] == 0:
                # 가로 파이프: 현재 셀과 왼쪽 셀만 0이면 가능
                # 이전 위치에 왼쪽에서 오는 경우와 이전 위치에 대각선에서 오는 경우를 합산
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]

                # 세로 파이프: 현재 셀과 위쪽 셀이 모두 0이어야 함
                # 이전 위치에 위쪽에서 오는 경우와 이전 위치에 대각선에서 오는 경우를 합산
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    # 최종 결과 출력
    # (N-1, N-1) 위치에 도달할 수 있는 모든 경우의 수를 합산
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()