import sys
input = sys.stdin.readline

n,m = map(int,input().split())
trues = set(list(map(int,input().split()))[1:]) # 진실을 아는 사람 리스트
party = []
cnt = []

for _ in range(m):
    data = set(map(int,input().split()[1:]))
    if data: # 참가자가 있으면
        party.append(data) # 해당 파티에 참가자 저장
        cnt.append(1) # 파티 수만큼 원소를 만들어줌

for _ in range(m):
    for i,p in enumerate(party): # 파티원 조사
        if trues & p: # 파티원 중 누군가가 진실을 알고있으면(집합 이용)
            cnt[i] = 0 # 해당 파티는 삭제
            trues |= p # |=는 업데이트. set 자료형에 

print(sum(cnt))