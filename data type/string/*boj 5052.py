import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    A = list(str(input().rstrip()) for _ in range(n)) # 전화번호 리스트
    A.sort() # 짧은 순으로 정렬
    
    for i in range(n-1):
        if A[i] == A[i+1][:len(A[i])]:
            print("NO")
            break
    else:
        print("YES")