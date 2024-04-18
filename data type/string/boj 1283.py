import sys
input = sys.stdin.readline

n = int(input())
set_ = set()
answer = []
for _ in range(n):
    tmp = input().rstrip()
    tmp_list= list(tmp.split())
    flag = False
    for i in range(len(tmp_list)):
        if tmp_list[i][0] not in set_:
            set_ |= {tmp_list[i][0].lower(),tmp_list[i][0].upper()}
            tmp_list[i] = "["+tmp_list[i][0]+"]"+tmp_list[i][1:]
            flag = True
        if flag:
            answer.append(' '.join(tmp_list))
            break
        
    else:
        for i in range(len(tmp_list)):
            for j in range(len(tmp_list[i])):
                if tmp_list[i][j] not in set_:
                    set_ |= {tmp_list[i][j].lower(),tmp_list[i][j].upper()}
                    tmp_list[i] = tmp_list[i][:j]+"["+tmp_list[i][j]+"]"+tmp_list[i][j+1:]
                    flag = True
                if flag:
                    answer.append(' '.join(tmp_list))
                    break
            if flag:
                break
        else:
            answer.append(tmp)

print('\n'.join(answer))