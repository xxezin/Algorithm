import sys
input = sys.stdin.readline
N,K = map(int,input().split())
A = list(map(int,input().split())) #

def quickSort(S,E,K): # Start, End, K
    global A
    if S < E :
        pivot = partition(S,E)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(S,pivot-1,K)
        else:
            quickSort(pivot+1,E,K)

def swap(i,j): # swap 함수 만들어주기
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(S,E):
    global A

    if S+1 == E: # 데이터가 2개인 경우
        if A[S] > A[E]: # 비교 후 return
            swap(S,E)
        return E

    # 데이터가 3개 이상인 경우
    M = (S+E)//2  # 중앙값
    swap(S,M) # 중앙값과 시작 위치 swap
    pivot = A[S] # pivot을 시작 위치 값인 A[S]로 저장
    i = S+1 # 시작 지점
    j = E # 종료 지점

    while i <= j:
        while pivot < A[j] and j>0: # 피벗보다 작은 수가 나올때까지 j 감소
            j = j-1
        while pivot > A[j] and i < len(A)-1: # 피벗보다 큰 수가 나올때까지 i 증가
            i = i+1
        if i<=j: # 찾은 i와 j 데이터를 swap
            swap(i,j)
            i +=1
            j -=1

    A[S] = A[j] # 피벗 데이터를 나눈 두 그룹의 경계 index 저장
    A[j] = pivot
    return j # 경계 index 리턴

quickSort(0,N-1,K-1) # 퀵 정렬 실행
print(A[K-1]) # K번째 데이터 출력
