import sys
input = sys.stdin.readline
result = 0

def mergeSort(s,e):
    global result,A

    if s<e:
        m = (s+e)//2
        mergeSort(s,m)
        mergeSort(m+1,e)

        a,b = s,m+1 # 두 그룹으로 나눔
        tmp = []

        while a <= m and b <= e:
            if A[a] <= A[b]:
                tmp.append(A[a])
                a+=1
            else:
                tmp.append(A[b])
                b+=1
                result += m-a+1
        
        if a<=m:
            tmp.append(A[a])
            a+=1
        if b<=e:
            tmp.append(A[b])
            b+=1

        for i in range(len(tmp)):
            A[s+i] = tmp[i]
        
n = int(input())
A = list(map(int,input().split()))
mergeSort(0,n-1)
print(result)