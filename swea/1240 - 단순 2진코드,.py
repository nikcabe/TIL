def is_valid_code(code):
    # 각 자리에서 홀수와 짝수를 처리하여 유효성을 검사하는 함수
    sum_v = 0
    for i, digit in enumerate(reversed(code)):
        if i % 2 == 0:
            sum_v += int(digit)
        else:
            sum_v += 3 * int(digit)
    return sum_v % 10 == 0

T = int(input())

for tc in range(1, 1+T):
    dic = {'0001101':'0','0011001':'1','0010011':'2','0111101':'3','0100011':'4','0110001':'5','0101111':'6','0111011':'7','0110111':'8','0001011':'9'}
    n,m = map(int, input().split())
    arr = [input() for _ in range(n)]

    bin = []
    a = []

    for i in range(n):
        for j in range(m-1, 5, -1):
            if arr[i][j] == '1':
                pattern = arr[i][j-7:j+1]
                if pattern in dic:
                    a.append(dic[pattern])
        if a:
            break

    if a:
        code = ' '.join(a)
        if is_valid_code(code):
            print(f"#{tc} {sum(int(d) for d in a)}")
        else:
            print(f"#{tc} 0")
    else:
        print(f"#{tc} 0")
