from collections import defaultdict
def solution(participant, completion):
    c = defaultdict(int)
    for i in completion:
        c[i] += 1
    for i in participant:
        if c[i] >= 1:
            c[i] -= 1
        else:
            return i

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))