## dictionary 이용
# import sys
# input = sys.stdin.readline

# n = int(input())
# dic = {}
# for i in range(n):
#     a = int(input())
#     if a in dic:
#         dic[a] +=1
#     else:
#         dic[a] = 1

# dic = dict(sorted(dic.items(), key=lambda x:(-x[1],x[0])))
# # print(next(iter(dic)))
# print(list(dic.keys())[0])

# 바킹독 응용
import sys
input = sys.stdin.readline

cnt,mxval,mxcnt = 0,-2**62-1,0
n = int(input())
A = [int(input()) for _ in range(n)]
A.sort()

for i in range(n):
    if i==0 or A[i]==A[i-1]:
        cnt +=1
    else:
        if cnt > mxcnt:
            mxcnt = cnt
            mxval = A[i-1]

        cnt = 1

if cnt > mxcnt:
    mxval = A[n-1]

print(mxval)