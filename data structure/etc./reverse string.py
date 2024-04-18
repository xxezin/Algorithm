# # 투포인터를 이용한 스왑
# def reverseString(self, s:List[str]) -> None:
#     left, right = 0, len(s)-1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left +=1
#         right -=1

s = ['안','녕','하','세','요']
s.reverse()
print(s)