n = int(input())
A = list(input().rstrip())

H = 0
for i in range(n):
    H += ((ord(A[i])-96)*((31)**(i))) % 1234567891
print(H)