while True:
    s = input().rstrip()
    if s == "#":
        break
    
    cnt = 0
    for i in ["a","e","i","o","u","A","E","I","O","U"]:
        cnt += s.count(i)
        
    print(cnt)