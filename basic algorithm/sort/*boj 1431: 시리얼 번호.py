## sort 함수 이용
# import sys
# input = sys.stdin.readline

# n = int(input())
# A = []

# for i in range(n):
#     a = input().rstrip()
#     A.append(a)

# def func(x):
#     tmp = 0
#     for i in x:
#         if i.isdigit():
#             tmp += int(i)
#     return tmp

# A = sorted(A, key=lambda x:(len(x),func(x),x))
# print('\n'.join(A))


## 직접 구현
import sys
input = sys.stdin.readline

n = int(input())
A = [input().rstrip() for _ in range(n)]

for i in range(n-1):
    for j in range(i+1,n):
        if len(A[i]) > len(A[j]):
            A[i],A[j] = A[j],A[i]

        elif len(A[i]) == len(A[j]):
            tmpi = 0
            tmpj = 0
            for x,y in zip(A[i],A[j]):
                if x.isdigit():
                    tmpi+=int(x)
                if y.isdigit():
                    tmpj+=int(y)
            
            if tmpi > tmpj:
                A[i],A[j] = A[j],A[i]

            elif tmpi == tmpj:
                for x,y in zip(A[i],A[j]):
                    if x > y:
                        A[i],A[j] = A[j],A[i]
                        break
                    elif x < y:
                        break

print('\n'.join(A))