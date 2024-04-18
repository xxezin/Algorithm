import copy
import sys
input = sys.stdin.readline

def find(A):
    answer = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if A[i][j] == ".":
                tmp += 1
            else:
                if tmp >= 2:
                    answer += 1
                    tmp = 0
                else:
                    tmp = 0
        if tmp >= 2:
            answer += 1
    return answer

n = int(input())
R = [list(input().rstrip()) for _ in range(n)]
C = copy.deepcopy(R)
C = list(map(list,zip(*C)))

print(find(R),find(C))