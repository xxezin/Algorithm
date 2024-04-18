A,B = map(str,input().split())

answer = 51
if len(A) == len(B): # 길이가 같을 때
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
    print(cnt)

else: # 길이가 다를 때
    for i in range(0,len(B)-len(A)+1):
        cnt = 0
        for j in range(len(A)):
            if A[j] != B[i:][j]:
                cnt += 1
        answer = min(answer,cnt)
    print(answer)