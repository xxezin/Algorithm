from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    n = sum(number) # 원하는 물품 갯수
    d = len(discount) # discount 길이
    
    for i in range(d-n+1):
        dic = defaultdict(int)
        for j in range(i,i+n):       
            dic[discount[j]] += 1
            
        for k in range(len(want)):
            if dic[want[k]] != number[k]:
                break
        else:
            answer+=1
                
    return answer

solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])