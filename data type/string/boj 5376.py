import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    tmp = list(input().split("."))
    tmp = tmp[1] # .뒷부분
    
    j = 0
    limit,inf = "",""
    while tmp[j] != "(":
        limit += tmp[j]
        j += 1
    
    if tmp[j] == "(":
        j += 1
        while tmp[j] != ")":
            inf += tmp[j]
            j += 1
    
    if limit != "":
        limit_n = int(limit)
        limit_d = 10**len(limit)

    if inf != "" :
        inf_n = int(inf)
        inf_d = 10**(len(inf))
    
    answer = 
        