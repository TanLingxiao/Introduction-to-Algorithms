import random

n = 10
# 构建初始队列
target = []
for _ in range(n):
    target.append(random.randint(0, 100))

print(target)

for i in range(len(target)-1):
    j = target.index(min(target[i:]))
    target[i], target[j] = target[j], target[i]
    print('step '+str(i+1)+': '+str(target))

print('result: ' + str(target))
