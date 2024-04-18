num, a = input().split()
a = int(a)
answer = 0
for i in range(len(num)):
    if num[i].isdigit():
        answer += int(num[i])*(a**(len(num)-1 -i))
    else:
        answer += int(ord(num[i])-55)*(a**(len(num)-1 -i))
print(answer)