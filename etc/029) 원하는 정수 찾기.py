## PSEUDO CODE ##
# N(수 개수 저장)
# A(수 데이터 리스트로 저장)
# A.sort() (정렬)
# M(탐색할 숫자 개수 저장)
# target_list(탐색할 수 데이터 리스트 저장)
#
# for M:
#     target(찾아야 하는 수)
#     # 이진 탐색 시작
#     start
#     end
#     while start <= end :
#         midi(중앙 인덱스)
#         midv(중앙 값)
#         if 중앙값 > target:
#             종료 인덱스 = 중앙 인덱스 -1
#         elif 중앙값 < target:
#             시작 인덱스 = 중앙 인덱스 +1
#         else:
#             찾았음, 반복문 종료
#
#     if (찾았으면) 1 출력,
#     else 0 출력

## CODE ##
N = int(input())
A = list(map(int,input().split()))
A.sort()
M = int(input())
target_list = list(map(int,input().split()))

for i in range(M):
    answer = False
    target = target_list[i]
    # 이진 탐색 시작
    start = 0
    end = N-1
    while start <= end:
        midi = (start+end)//2
        midv = A[midi]
        if midv > target:
            end = midi -1
        elif midv < target:
            start = midi +1
        else:
            answer = True
            break
    if answer:
        print(1)
    else:
        print(0)