paper = input().rstrip()
word = input().rstrip()

# 방법 1.
# i = 0
# cnt = 0
# n = len(word)
# while i < len(paper):
#     if paper[i:i+n] == word:
#         cnt += 1
#         i += n
#     else:
#         i += 1

# print(cnt)

# 방법 2. 파이썬다운 방식
print(paper.count(word))