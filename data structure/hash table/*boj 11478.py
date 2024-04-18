s = input()
dic = {}
for i in range(len(s)):
    for j in range(i,len(s)):
        dic[s[i:j+1]] = 1

print(len(dic))