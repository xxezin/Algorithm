from string import ascii_lowercase
def solution(s, skip, index):
    answer = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    
    dic = {alpha:idx for idx,alpha in enumerate(a_to_z)}
    
    for i in range(len(s)):
        answer += a_to_z[(dic[s[i]]+index) % len(a_to_z)]
    return answer