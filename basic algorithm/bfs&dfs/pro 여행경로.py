from collections import defaultdict
def solution(tickets):
    answer = []
    airport = defaultdict(list)
    vis = defaultdict(int)
    
    for a,b in tickets:
        airport[a].append(b)
    
    for i in airport.keys():
        airport[i].sort(reverse=True)
    
    answer = []
    def dfs(v):
        while airport[v]:
            dfs(airport[v].pop())
        answer.append(v)
        
    dfs("ICN")
    
    return answer[::-1]

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])