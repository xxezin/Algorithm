def solution(msg):
    dic = {chr(65+i): i+1 for i in range(26)}

    i = 0
    check = ''
    result = []
    num = 27
    
    while i < len(msg):
        check += msg[i]
        if check in dic:
            i += 1
        else:
            dic[check] = num
            num +=1
            result.append(dic[check[:-1]])
            check=''
            
    result.append(dic[check])
    return result

solution("KAKAO")