import random

n = 10
# 构建初始队列
target = []
for _ in range(n):
    target.append(random.randint(0, 100))

print(target)

print("after sorted....")


def binary_search(A, left, right, x):
    if right >= left:
        mid = int(left + (right - left)/2)
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return binary_search(A, left, mid-1, x)
        else:
            return binary_search(A, mid+1, right, x)
    else:
        return -1


place = binary_search(target, 0, len(target)-1, 2)
print(place)