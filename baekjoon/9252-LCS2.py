a = list(input())
b = list(input())

# DP 테이블 초기화 (크기는 (len(a)+1) x (len(b)+1))
dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

# DP 테이블 채우기
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            # 문자가 같으면 대각선 위 값에 1을 더함
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # 문자가 다르면 왼쪽이나 위쪽 값 중 큰 값
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

result = dp[len(a)][len(b)]

lcs = []
i, j = len(a), len(b)

while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        lcs.append(a[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

lcs.reverse()  # 역추적하면서 수열이 뒤집혔으므로 반전

# 결과 출력
print(result)
print(''.join(lcs))
