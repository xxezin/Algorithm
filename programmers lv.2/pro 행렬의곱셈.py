# def solution(A,B):
#     return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]


A = [[1, 4], [3, 2], [4, 1]]
B = [[1,2,3], [3,4,5],[6,7,8]]

for i in zip(*B):
    print(i)