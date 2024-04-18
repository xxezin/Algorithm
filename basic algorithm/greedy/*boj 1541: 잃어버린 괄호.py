# 괄호를 적절히 쳐서 이 식의 값을 최소로 만든다

# 식은 0~9, +, - 만으로 이루어져 있다
# 가장 처음과 마지막 문자는 숫자이다
# 수는 0으로 시작할 수 있다
# 식의 길이는 50보다 작거나 같다

# - 뒤에 있는 숫자를 괄호로 묶으면 됨

a = input().split('-')
ans = 0

for i in a[0].split('+'):
    ans += int(i)

for i in a[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)