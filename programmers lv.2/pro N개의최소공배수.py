def solution(arr):
    answer = arr[0]
    from math import gcd
    for num in arr:
        answer = answer*num // gcd(answer,num)
    return answer
solution([2,6,8,14])