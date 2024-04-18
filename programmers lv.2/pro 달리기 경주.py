def solution(players, callings):
    answer = []
    for called in callings:
        tmp = players.index(called)
        players[tmp],players[tmp-1] = players[tmp-1],players[tmp]
    return answer

solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])