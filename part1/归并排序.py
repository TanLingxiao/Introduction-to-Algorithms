import random

n = 10
# 构建初始队列
target = []
for _ in range(n):
    target.append(random.randint(0, 100))

print(target)

print("after sorted....")


def merge(left: list, right: list):
    print('left: ' + str(left) + ' right: ' + str(right))
    result = []
    while left and right:
        min_val = left.pop(0) if left[0] < right[0] else right.pop(0)
        result.append(min_val)
    result += left if left else right
    return result


def merge_sort(A: list):
    if len(A) <= 1:
        result = A
    else:
        mid = len(A) // 2
        left, right = merge_sort(A[:mid]), merge_sort(A[mid:])
        result = merge(left, right)
    return result


print('result: '+str(merge_sort(target)))
