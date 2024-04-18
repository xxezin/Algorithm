import sys
input = sys.stdin.readline

start, end, quit = input().split()
start = int(start[:2])*100 + int(start[3:])
end = int(end[:2])*100 + int(end[3:])
quit = int(quit[:2])*100 + int(quit[3:])

dic = {}
cnt = 0
while True:
    try:
        time, name = input().split()
        time = int(time[:2])*100 + int(time[3:])
        if time <= start:
            dic[name] = 1
        elif end <= time <= quit and name in dic:
            del dic[name]
            cnt += 1
    except:
        break
    
print(cnt)