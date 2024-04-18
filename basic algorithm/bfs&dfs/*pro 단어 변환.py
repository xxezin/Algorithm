from collections import deque
def solution(begin, target, words):
    q = deque()
    n = len(words)
    b = len(begin)
    
    def can_change(word,change): # 몇개의 요소가 다른지 비교
        diff = 0
        for i in range(b):
            if word[i] != change[i]:
                diff += 1
                
        if diff == 1:
            return True
        else:
            return False
        
    def bfs():
        if target not in words:
            return 0
        q.append((begin,0))

        while q:
            word, depth = q.popleft()
            for change in words:
                if can_change(word,change): # 한개의 요소만 달라 바꿀 수 있으면
                    if change == target: # 바뀌는게 타겟과 같으면
                        return depth + 1
                    else:
                        q.append((change,depth+1))
                        
    return bfs()