import sys
input = sys.stdin.readline

def dfs(depth,root):
    curs = sorted(root)
    
    for cur in curs:
        print("--" * depth,cur,sep='')
        dfs(depth + 1, root[cur]) # 다음 노드로
        
ROOT = dict()
n = int(input())

for _ in range(n):
    txt = input().split()[1:]
    cur = ROOT
    for info in txt:
        if info in cur:
            pass
        else:
            cur[info] = dict()
            
        cut = cur[info]

dfs(0,ROOT)