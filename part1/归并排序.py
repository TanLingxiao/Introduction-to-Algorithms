import random
import math

n = 10
# 构建初始队列
target = []
for _ in range(n):
    target.append(random.randint(0, 100))

print(target)

print("after sorted....")

def merge_sort(A: list, p: int, r: int) ->list:
    q = math.floor((p + r)/2)
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    