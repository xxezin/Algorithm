def solution(numbers, hand):
    answer = ''
    phone = {1:[0,0],2:[0,1],3:[0,2],
          4:[1,0],5:[1,1],6:[1,2],
          7:[2,0],8:[2,1],9:[2,2],
          '*':[3,0],0:[3,1],'#':[3,2]}
    
    # 초기 위치
    l_hand = '*'
    r_hand = '#'
    
    for num in numbers:
        if num in [1,4,7]: # 왼손 사용 경우
            answer += "L"
            l_hand = num
            
        elif num in [3,6,9]: # 오른손 사용 경우
            answer += "R"
            r_hand = num
        
        else: # 2,5,8,0의 경우
            l_dis, r_dis = 0,0
            
            # 좌표 거리 계산
            l_dis = abs(phone[num][0]-phone[l_hand][0]) + abs(phone[num][1]-phone[l_hand][1])
            r_dis = abs(phone[num][0]-phone[r_hand][0]) + abs(phone[num][1]-phone[r_hand][1])
            
            # 왼손이 더 가까우면
            if l_dis < r_dis:
                answer += "L"
                l_hand = num
            
            # 오른손이 더 가까우면
            elif r_dis < l_dis:
                answer += "R"
                r_hand = num
            
            # 거리가 같으면 어떤 손 잡이냐에 따라
            elif r_dis == l_dis:
                if hand == "right":
                    answer += "R"
                    r_hand = num
                else:
                    answer += "L"
                    l_hand = num
                   
            
    return answer