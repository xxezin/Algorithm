N = int(input()) # 탑 개수
A = list(map(int,input().split())) # 탑 높이 배열
stack = [] # 탑 높이와 인덱스 한번에 저장

for i in range(N): # 탑 높이 배열의 수를 하나씩 스택에 추가해본다.
    while stack and stack[-1][0] < A[i]: # 현재 탑 배열보다 작은 수들은 pop. why? 영향을 주지 않음
        stack.pop() 
    if stack: # 스택이 있으면 신호를 수신하는 탑이 있음
        print(stack[-1][1], end=' ')
    else:
        print(0,end = ' ') 
    stack.append([A[i],i+1])
    
