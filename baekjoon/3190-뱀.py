# 서건호

## 미안하다.. 시간부족으로
## 다른 사람의 코드를 가져왔다
## 물론 내가 다시 한번 써봄

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

d = 0 # 0 : D, 1: L
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 2

l = int(input())
turn_info = []
for _ in range(l):
    t, c = input().split()
    turn_info.append((int(t), c))

def rotate(c):
    global d
    if c == 'D':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
count = 0
turn_index = 0
sx, sy = 0, 0
graph[0][0] = 1
snake = []
snake.append((0, 0))

while True:
    count += 1
    nx = sx + dx[d]
    ny = sy + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 2:
            snake.append((nx, ny))
            graph[nx][ny] = 1
            sx, sy = nx, ny
        elif graph[nx][ny] == 1:
            break
        elif graph[nx][ny] == 0:
            tx, ty = snake.pop(0)
            graph[tx][ty] = 0
            snake.append((nx, ny))
            graph[nx][ny] = 1
            sx, sy = nx, ny
    else:
        break
    if turn_index < l:
        if count == turn_info[turn_index][0]:
            rotate(turn_info[turn_index][1])
            turn_index += 1


print(count)