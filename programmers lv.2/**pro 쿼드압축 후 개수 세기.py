def solution(arr):
    answer = [0,0]
    def func(a,b,l):
        value = arr[a][b]
        for i in range(a,a+l):
            for j in range(b,b+l):
                if arr[i][j] != value:
                    l //=2
                    func(a,b,l)
                    func(a,b+l,l)
                    func(a+l,b,l)
                    func(a+l,b+l,l)
                    return
        answer[value] += 1
    func(0,0,len(arr))
    return answer

solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])