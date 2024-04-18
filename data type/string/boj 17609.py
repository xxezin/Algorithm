import sys
input = sys.stdin.readline

def palind(s,e,tmp):
    while s <= e:
        if str[s] == str[e]:
            s += 1
            e -= 1
        else:
            if tmp == 0:
                left = palind(s+1,e,tmp+1)
                right = palind(s,e-1,tmp+1)
                return min(left,right)
            else: # 두번 이상 바꿔야하니까
                return 2
    return tmp

T = int(input())
for _ in range(T):
    str = input().strip()
    s,e = 0,len(str)-1
    print(palind(s,e,0))