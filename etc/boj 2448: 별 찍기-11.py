n = int(input())

def draw(n):
    if n==3:
        return ['  *  ',' * * ','*****']
    Stars = draw(n//2)
    A = []
    for s in Stars:
        A.append(' '*(n//2)+s+' '*(n//2))
    for s in Stars:
        A.append(s+' '+s)

    return A

draw(n)
print('\n'.join(draw(n)))