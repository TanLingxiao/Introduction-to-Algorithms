import random
from typing import List

# 采用分治策略

n = 20
# 构建初始队列
target = []
for _ in range(n):
    target.append(random.randint(-50, 50))

print(target)


def find_maxsum(A: List[int], low: int, high: int):
    if low == high:
        return A[low]
    mid = (high + low) // 2
    left_sum = find_maxsum(A, low, mid)
    right_sum = find_maxsum(A, mid+1, high)
    now_left = A[mid]
    left = A[mid]
    for i in range(mid - 1, low - 1, -1):
        now_left = now_left + A[i]
        if now_left > left:
            left = now_left
    now_right = A[mid + 1]
    right = A[mid + 1]
    for j in range(mid + 2, high + 1):
        now_right = now_right + A[j]
        if now_right > right:
            right = now_right
    result = max(left_sum, right_sum, left + right)
    return result


res = find_maxsum(target, 0, len(target)-1)
print('max is: ' + str(res))
