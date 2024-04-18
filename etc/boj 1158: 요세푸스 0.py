# 요세푸스 순열(원에서 사람들이 제거되는 순서)을 구하는 프로그램
# 1~N번까지 N명의 사람이 원을 이루며 앉아있고, 양의 정수 K(<=N)가 주어짐
# 순서대로 K번째 사람을 제거함
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 과정을 수행함
# N명의 사람이 모두 제거될 때까지 계속됨

# 입력 : N,K(1<=K<=N<=5,000)
# 출력 : 요세푸스 순열(원에서 사람들이 제거되는 순서)

from collections import deque
n,k = map(int,input().split())
q = deque(list(range(1,n+1)))
result = []

i=0
while q:
    i+=1
    tmp = q.popleft()
    if i %k !=0: # k로 나누어 0이 아닌 경우 = 차례가 아닌 경우 뒤로 붙여줌
        q.append(tmp)
    else:
        result.append(tmp)

print('<'+', '.join(map(str,result))+'>')