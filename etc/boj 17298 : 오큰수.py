## pseudo code
# N : 수의 개수
# A : 수열 리스트
# stack : 스택 []
# answer = [-1]*N -1을 default로. 있는 애들만 오큰수로 채워준다.

# for N :
#     while stack이 있고 A[stack[-1]]이 현재 수보다 작으면:
#        현재 수가 오큰수
#     stack.append(인덱스로)

# print(*___)을 하면 공백을 사이로 내용물만 뱉음!

N = int(input())
A = list(map(int,input().split()))
ans = [-1]*N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(*ans)

