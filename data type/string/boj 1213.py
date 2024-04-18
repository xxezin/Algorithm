# import sys
# from collections import Counter
# input = sys.stdin.readline

# s = list(input().rstrip())
# s.sort()
# count = Counter(s)

# odd = 0 # 홀수 개수
# center = "" # 홀수 문자

# for k,v in count.items():
#     if v %2 != 0:
#         odd += 1
#         center += k
#         s.remove(k) # 홀수 문자 하나 제거
        
#     if odd > 1: # 홀수 문자가 2개 이상이면 팰린드롬 불가
#         break
    
# if odd > 1:
#     print("I'm Sorry Hansoo")
# else:
#     left = ""
#     for i in range(0,len(s),2):
#         left += s[i]
        
#     print(left + center + left[::-1])

from collections import Counter
s = input().strip()
dic = Counter(s)

ans,center = "",""
for k,cnt in sorted(dic.items()):
    if cnt %2: # 홀수면
        if center != "": # 홀수인게 이미 있었으면
            print("I'm Sorry Hansoo")
            break
        center = k
    ans += k*(cnt//2)

else:
    print(ans+center+ans[::-1])