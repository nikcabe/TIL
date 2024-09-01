T = int(input())

for tc in range(1, 1 + T):
    d, a, b, f = map(float, input().split())
    print(f'#{tc} {d / (a + b) * f}')