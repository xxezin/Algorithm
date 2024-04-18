h,w = map(int,input().split())
A = list(map(int,input().split()))

left, right = 0, len(A)-1
left_max, right_max = A[left], A[right]

volume = 0
while left < right:
    left_max = max(left_max, A[left])
    right_max = max(right_max, A[right])

    if left_max <= right_max:
        volume += left_max - A[left]
        left += 1
    else:
        volume += right_max - A[right]
        right -= 1

print(volume)