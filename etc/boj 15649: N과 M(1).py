n,m = map(int,input().split())
# answer = []

# def func():
#     if len(answer)==m:
#         print(" ".join(map(str,answer)))
#         return
    
#     for i in range(1,n+1):
#         if i not in answer:
#             answer.append(i)
#             func()
#             answer.pop()

# func()


arr = [0]*(m)
used = [False]*(n+1)
def back(k):
    if k==m: # 만약 해당하는 답이면 출력
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,n+1): # 아니면 탐색
        if not used[i]:
            used[i] = True
            arr[k] = i
            back(k+1)
            used[i] = False


back(0)