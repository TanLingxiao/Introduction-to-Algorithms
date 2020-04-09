import random

n = 10
# 构建初始队列
target = []
for _ in range(n):
    target.append(random.randint(0, 100))

print(target)

print("after sorted....")

# 从小到大插入排序
for i in range(len(target)-1):
    j = i + 1
    key = target[j]
    while target[i] > key and i > -1:
        target[i+1] = target[i]
        i = i - 1
    target[i+1] = key
    print('step '+str(j)+': '+str(target))

print('result: ' + str(target))
