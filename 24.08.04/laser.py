T = int(input())

for tc in range(1,1+T):
    laser = input()
    i = 0
    stick = 0
    sti_stk = 0
    while i < len(laser):
        if laser[i] == '(':
            if laser[i+1] == ')':
                sti_stk += stick
                i += 2
            else:
                stick += 1
                i += 1
        else:
            stick -= 1
            i += 1
            sti_stk += 1
    print(f'#{tc} {sti_stk}')
