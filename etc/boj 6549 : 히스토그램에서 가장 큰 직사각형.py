A = []
while True:
    A = list(map(int,input().split()))
    if A == [0]:
        break
    N = A[0]
    stack = []
    answer = 0

    for i in range(1,N+1):
        idx = i
        while stack and stack[-1][0] >= A[i]:
            answer = max(answer, 1*(i-stack[-1][1])*stack[-1][0])
            idx = stack[-1][1]
            stack.pop()

        stack.append([A[i],idx])
    while stack:
        answer = max(answer, 1*(N+1-stack[-1][1])*stack[-1][0])
        stack.pop()
    
    print("{}".format(answer))