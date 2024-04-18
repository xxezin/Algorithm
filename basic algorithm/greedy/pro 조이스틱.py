def solution(name):
    answer = 0
    mylist = list(map(str,name))
    min_move = len(name)-1
    next_idx = 0
    
    for idx,char in enumerate(mylist) :
        answer += min(ord(char)-ord('A'),ord('Z')-ord(char)+1)
        next_idx = idx+1
        while next_idx < len(name) and name[next_idx] == 'A': # ㅁ면 움직일 필요 없으니
            next_idx += 1

        min_move = min(min_move, 2*idx + len(name) - next_idx, idx+2*(len(name)-next_idx))
            
    answer += min_move         
    return answer

solution("JAN")