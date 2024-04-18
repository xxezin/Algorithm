## PSEUDO CODE ##
# N(노드 개수)
# A(그래프 데이터 저장 인접 리스트)
#
# for N만큼 반복:
#     A 인접 리스트에 그래프 데이터 저장
#
# visited 리스트
# distance 리스트
#
# BFS:
#     큐 자료구조에 시작노드 삽입
#     visited 리스트에 현재 노드 방문 기록
#     while 큐:
#         큐에서 노드 데이터 가져오기
#         for 현재 노드의 연결 노드 :
#             if 미방문 노드면:
#                 큐에 데이터 삽입
#                 visited 리스트에 방문 기록
#                 큐에 삽입된 노드 거리 = 현재 노드의 거리 + 엣지 가중치
#
# BFS(처음 시작점) 실행
# distance 리스트에서 가장 큰값을 지닌 노드 시작점 설정
# visited 리스트 초기화
# distance 리스트 초기화
# BFS(새로운 시작점으로) 실행
# distance 리스트에서 가장 큰 수를 정답으로 출력


## CODE ##
from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
    Data = list(map(int,input().split()))
    index = 0
    S = Data[index]
    index +=1
    while True:
        E = Data[index]
        if E == -1:
            break
        V = Data[index+1]
        A[S].append((E,V))
        index+=2

distance = [0]*(N+1)
visited = [False]*(N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_Node]+i[1]

# 임의로 1에서 시작
BFS(1)
Max = 1
for i in range(2,N+1):
    if distance[Max] < distance[i]:
        Max = i
# 초기화
distance = [0]*(N+1)
visited = [False]*(N+1)

BFS(Max)
distance.sort()
print(distance[N])