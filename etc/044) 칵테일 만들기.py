N = int(input())
A = [[] for _ in range(N)]
visited = [False]*(N)
D = [0]*(N) # 각 노드값 저장 리스트
lcm = 1 # 최소 공배수

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v]*i[2]//i[1]
            DFS(next)

for i in range(N-1):
    a,b,p,q = map(int,input().split())
    A[a].append((b,p,q))
    A[b].append((a,q,p))
    lcm *= (p*q//gcd(p,q))

D[0] = lcm # 0번 노드에 최소 공배수 저장 # 임의로 0번을 택한 것일뿐
DFS(0) # DFS 수행
mgcd = D[0]

for i in range(1,N):
    mgcd = gcd(mgcd,D[i]) # DFS를 통해 업데이트된 D 리스트 값들의 최대 공약수 계싼

for i in range(N):
    print(int(D[i]//mgcd), end=' ') # D 리스트의 각 값을 최대 공약수로 나눠 정답 출력

