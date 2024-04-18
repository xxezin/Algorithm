def solution(number, k):
    answer = ''
    nums = list(map(int,number))
    nums.sort(reverse=True)
    nums = nums[:len(number)-k]
    for num in nums:
        num = str(num)
        answer += num

    return answer

solution("19232344",2)