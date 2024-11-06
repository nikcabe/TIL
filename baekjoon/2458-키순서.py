# 플로이드 워셜


N,M = map(int, input().split())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    tall, short = map(int,input().split())
    arr[tall][short] = 1

# 경유지
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            # 이어져 있는 곳을 파악
            if arr[i][j] == 1 or (arr[i][k] and arr[k][j]):
                arr[i][j] = 1

answer = 0
for i in range(1,N+1):
    total_per = 0
    for j in range(1,N+1):
        # 자신보다 작은 사람과 큰 사람의 합
        total_per += arr[i][j] + arr[j][i]
    # 자신보다 작은 사람과 큰 사람의 합이 N-1일경우 자신의 위치를 앎
    if total_per == N-1:
        answer+=1

print(answer)