import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    a,b,c,d = map(int,input().split())
    A.append([a*100+b,c*100+d])
A.sort(key=lambda x:(x[0],x[1])) # 피는 날짜 빠른순으로 정렬 후, 지는 날짜 빠른 순으로 정렬

cnt = 0 # 선택한 꽃 개수
end = 301 # 현재 꽃 지는 시간

while A:
    if end >= 1201 or A[0][0] > end:
        break

    nxt_end = -1

    for i in range(len(A)):
        if A[0][0] <= end: # 현재 꽃 지는 시간 이전에 피는 꽃 중에
            if nxt_end <= A[0][1]:
                nxt_end = A[0][1] # 가장 늦게 지는 꽃 추출

            A.remove(A[0]) # 봤으면 삭제
        else:
            break

    end = nxt_end
    cnt +=1


if end < 1201:
    print(0)
else:
    print(cnt)