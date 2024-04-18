import sys
input = sys.stdin.readline

n,k = map(int,input().split())
A = list(map(int,input().split()))
plug = []
result = 0

for i in range(k):
    # 이미 꽂혀있을 때
    if A[i] in plug:
        continue
    
    # 빈자리가 있을 때
    if len(plug) != n:
        plug.append(A[i])
        continue
    

    far = 0 # 가장 멀리 있는 플러그
    temp = 0
    # 플러그에 꽂힌 기기들에 대해 검사
    for p in plug:
        # 앞으로 사용할 목록에 없으면
        if p not in A[i:]:
            temp = p
            break

        # 현재 가장 먼 사용 기기보다 더 늦게 사용되면
        elif A[i:].index(p) > far:
            far = A[i:].index(p)
            temp = p
    
    plug[plug.index(temp)] = A[i] # 늦게 사용되거나 사용할 목록이 없는 애한테 꽂아줌
    result +=1

print(result)