# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

# 코드 1: 병합 정렬을 구현해봄
import sys
input = sys.stdin.readline
# print = sys.stdout.write

n = int(input())
A = [['',''] for _ in range(n)]
for i in range(n):
    A[i][0] = str(input().rstrip())
    A[i][1] = (len(A[i][0]))

def mergesplit(data):
    if len(data) <= 1:
         return data
    
    medium = int(len(data)/2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])

    return merge(left,right)

def merge(left,right):
    i,j = 0,0
    merged = []

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            merged.append(left[i])
            i +=1
        elif left[i][1] > right[j][1]:
            merged.append(right[j])
            j +=1
        else:
            if left[i][0] == right[j][0]:
                merged.append(left[i])
                i+=1
                j+=1
            elif left[i][0] < right[j][0]:
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1

    while i < len(left):
        merged.append(left[i])
        i +=1

    while j < len(right):
        merged.append(right[j])
        j +=1

    return merged


ans = mergesplit(A)
for i in range(len(ans)):
    print(ans[i][0])

# 시간 : 54분 소요