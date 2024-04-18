# 잔재미코딩 연습문제 1
# def recursive(k):
#     print(int(k))
#     if k==1:
#         return
    
#     else:
#         if k %2 !=0: # 홀수면
#             recursive(3*k+1)
#         else:
#             recursive(k/2)

# recursive(3)



# 잔재미코딩 연습문제 2
def recursive(k):
    if k==1:
        return 1
    elif k==2:
        return 2
    elif k==3:
        return 4

    return recursive(k-1)+recursive(k-2)+recursive(k-3)

recursive(5)