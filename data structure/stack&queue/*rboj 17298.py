n = int(input())
A = list(map(int,input().split()))
ans = [-1]*n

stack = []
# ver.1
# for i in range(n):
#     while stack and stack[-1][0] < A[i]:
#         ans[stack.pop()[1]] = A[i]
              
#     stack.append([A[i],i])

# ver.2
for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    
    stack.append(i)
    
print(*ans)