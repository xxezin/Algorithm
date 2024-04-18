import sys
input = sys.stdin.readline
def falindrome(v):
    if v[:] == v[::-1]:
        return True
    
    return False

if __name__ == '__main__':
    while True:
        tmp = str(input().rstrip())
        if tmp == "0":
            break
        
        if falindrome(tmp):
            print("yes")
        else:
            print("no")