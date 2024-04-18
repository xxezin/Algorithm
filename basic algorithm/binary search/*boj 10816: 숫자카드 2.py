# 이분탐색 활용
import sys
input = sys.stdin.readline

def binary_search(data,search,start,end):
    if start>end:
        return 0 # 못 찾은 경우 0 추출
    mid = (start+end)//2
    if data[mid] == search:
        return cnt.get(search) # 찾는 수와 같으면 딕셔너리에서 값 추출
    elif data[mid] > search:
        return binary_search(data,search,start,mid-1)
    else:
        return binary_search(data,search,mid+1,end)

n = int(input())
A = sorted(list(map(int,input().split())))

m = int(input())
B = list(map(int,input().split()))

cnt = {}
for i in A: # 딕셔너리에 갯수 저장
    if i in cnt:
        cnt[i] +=1
    else:
        cnt[i] =1

for i in B: # 찾는 수 이분탐색
    print(binary_search(A,i,0,len(A)-1),end=' ')

# # python dictionary 활용

# check = {}
# for i in A:
#     if i in check:
#         check[i] +=1
#     else:
#         check[i] = 1

# for i in B:
#     if i in check:
#         print(check[i],end=' ')
#     else:
#         print(0,end=' ')