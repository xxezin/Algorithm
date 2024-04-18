import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s,e):
    if e-s < 1 : return # 수가 1일때는 그대로 리턴
    m = int((s+e)/2)
    merge_sort(s,m)
    merge_sort(m+1,e)
    for i in range(s,e+1):
        tmp[i] = A[i]
    k = s # 오름차순으로 정렬될 새로운 리스트의 인덱스
    index1 = s # 첫번째 그룹 시작점
    index2 = m+1 # 두번째 그룹 시작점
    while index1 <= m and index2 <= e: # 두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k +=1
            index2 +=1
        else :
            A[k] = tmp[index1]
            k +=1
            index1 +=1
    # 한쪽 그룹이 다 선택되었을때 남아있는 값 정리
    while index1 <= m:
        A[k] = tmp[index1]
        k+=1
        index1 +=1
    while index2 <= e:
        A[k] = tmp[index2]
        k+=1
        index2+=1

N = int(input())
A = [0]*int(N+1)
tmp = [0]*int(N+1)

for i in range(1,N+1):
    A[i] = int(input())

merge_sort(1,N)

for i in range(1,N+1):
    print(str(A[i])+'\n')