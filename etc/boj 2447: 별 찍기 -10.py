n = int(input())

def draw(n):
    if n==1:
        return ['*']
    Stars = draw(n//3)
    A = []

    for star in Stars:
        A.append(star*3)
    for star in Stars:
        A.append(star+' '*(n//3)+star)
    for star in Stars:
        A.append(star*3)

    return A

print('\n'.join(draw(n)))