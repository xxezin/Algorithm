# 1. 현재 q의 가장 앞에 있는 문서의 '중요도' 확인
# 2. 나머지 문서 중 현재 문서보다 중요도가 높은 문서가 있다면,
#     이 문서를 인쇄하지 않고 q의 맨 마지막에 재배치함. 그렇지 않다면 바로 인쇄

# 입력 : 테스트 케이스 수, 각 테스트 케이스는 두줄로 이뤄져 있음
#                     1) 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 q에 몇번째에 있는지
#                         (여기서 맨 왼쪽이 0번째)
#                     2) N개 문서의 중요도가 차례대로 주어짐


from collections import deque
import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 수
for _ in range(t):
    n,m = map(int,input().split()) # 문서 개수, 궁금한 문서의 현재 순서
    q = deque(map(int,input().split())) # N개 문서의 중요도
    q = deque([i,idx] for idx,i in enumerate(q)) # idx도 같이 저장
    cnt = 0

    while True:
        if q[0][0] == max(q, key=lambda x:x[0])[0]:
            cnt +=1
            if q[0][1]==m: # 원하던 m번째 문서라면!
                print(cnt)
                break
            else: # 아니면 그냥 팝
                q.popleft()
        
        else: # 맥스 아니면 뒤로 붙여줌
            q.append(q.popleft())