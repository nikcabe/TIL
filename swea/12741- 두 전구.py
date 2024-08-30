T = int(input())
results = []

for tc in range(1, 1+T):
    a, b, c, d = map(int, input().split())
    x = min(b, d)
    y = max(a, c)
    if x < y:
        result = 0
    else:
        result = x-y
    results.append(f'#{tc} {result}')
print("\n".join(results))