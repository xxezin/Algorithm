import sys
input = sys.stdin.readline

n = int(input())
heap = [0]*(1000001)
size = 0

def push(x):
    global size
    size += 1
    heap[size] = x

    idx = size
    while idx != 1:
        par = int(idx/2)
        if heap[par] <= heap[idx]:
            break

        heap[par],heap[idx] = heap[idx],heap[par]
        idx = par

def top():
    return heap[1]

def pop():
    global size
    print(heap[1])
    heap[1] = heap[size] # 트리의 마지막 위치와 바꿈(어쨌든 마지막 위치의 자식은 없으니 트리의 구조 유지)
    size -=1 
    idx = 1

    while 2*idx <= size: # 다 꼬였으니 정리를 좀 해보자. 일단 자식부터
        left = 2*idx # 왼쪽 자식
        right = 2*idx+1 # 오른쪽 자식
        min_c = left # 두 자식 중 작은 값의 인덱스

        if right <= size and heap[right] < heap[left]: # 만약 right 자식이 reft 자식보다 작으면
            min_c = right # 두 자식 중 작은 값의 인덱스를 right 자식으로 바꿔줌
        if heap[idx] <= heap[min_c]: # 비교해서 현재 값이 더 작은 값이면(최소힙이니) 냅둬
            break
        # 만약 현재 값이 자식 값보다 크면 둘이 바꿈
        heap[idx],heap[min_c] = heap[min_c],heap[idx]
        idx = min_c # 자식


for i in range(n):
    tmp = int(input())
    if tmp==0:
        if size==0:
            print(0)
        else:
            pop()
    else:
        push(tmp)