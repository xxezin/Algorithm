n = int(input())

mx, mx_idx = 0,0
A = sorted([tuple(map(int,input().split())) for _ in range(n)],key=lambda x:x[0])
for i in range(n):
    if mx < A[i][1]:
        mx = A[i][1]
        mx_idx = i

answer = mx # 가장 높은 기둥 높이 * 1
left,right = [0],[n-1]

for i in range(mx_idx+1):
    if A[left[-1]][1] < A[i][1]:
        left.append(i)

prev = A[left.pop()][0]
while left:
    now = left.pop()
    answer += (prev-A[now][0]) * A[now][1]
    prev = A[now][0]

for j in range(n-2,mx_idx-1,-1):
    if A[right[-1]][1] <= A[j][1]:
        right.append(j)

prev = A[right.pop()][0]
while right:
    now = right.pop()
    answer += (A[now][0]-prev) * A[now][1]
    prev = A[now][0]

print(answer)