# 구현 문제
import re
def solution(new_id):
    new_id = new_id.lower() # 소문자로 치환
    new_id = re.sub('[^a-z0-9\-_.]','',new_id) # ... 를 제외(^)한 모든 문자 제거
    new_id = re.sub('\.+','.',new_id) # 마침표(.)가 두번 이상 연속된 부분 하나로 치환
    new_id = re.sub('^[.]|[.]$', '',new_id)
    new_id = "a" if len(new_id) == 0 else new_id[:15]
    new_id = re.sub('^[.]|[.]$', '',new_id)
    new_id = new_id if len(new_id) > 2 else new_id+"".join(new_id[-1] for i in range(3-len(new_id)))
    return new_id