import sys
input = sys.stdin.readline

def bubblesort(array):
    for i in range(len(array)-1):
        swap = False
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swap = True

        if not swap:
            break

n = int(input())
A = [0]*n
for i in range(n):
    A[i] = int(input())

bubblesort(A)
for i in range(n):
    print(A[i])