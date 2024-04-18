n = list(map(int,str(input())))
ans = [0 for _ in range(10)]

for i in n:
    if i not in (6,9):
        ans[i] +=1
    
    else:
        if i == 6:
            if ans[i] <= ans[9]:
                ans[i] +=1
            elif ans[i] > ans[9]:
                ans[9] +=1
        elif i == 9:
            if ans[i] <= ans[6]:
                ans[i] +=1
            elif ans[i] > ans[6]:
                ans[6] +=1

print(max(ans))