import itertools, math
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    lst = []
    for i in range(len(numbers)):
        for j in itertools.permutations(numbers,i+1):
            lst.append(''.join(map(str,j))) # 종이 조각들 조합 리스트
    
    for i in range(len(lst)):
        lst[i] = int(lst[i]) # int로 바꿔줌
    lst = list(set(lst))
    
    sosu = [0]*(max(lst)+1)
    for i in range(2,max(lst)+1):
        sosu[i] = i
        
    for i in (2,int(math.sqrt(max(lst)+1))+1):
        if sosu[i] == 0:
            continue
            
        for j in range(i+i,max(lst)+1,i):
            sosu[j] = 0
    
    for i in lst:
        if sosu[i] != 0:
            answer += 1
    return answer

solution("17")