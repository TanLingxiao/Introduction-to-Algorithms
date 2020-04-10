import random

n = 10
# 构建初始队列
target = []
for _ in range(n):
    target.append(random.randint(0, 100))

print(target)

print("after sorted....")

for i in range(n-1):
    for j in range(0, n-i-1):
        if target[j] > target[j+1]:
            target[j], target[j+1] = target[j+1], target[j]

print(target)