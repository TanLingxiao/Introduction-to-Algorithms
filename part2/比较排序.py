import random


n = 20
target = []
for _ in range(n):
    target.append(random.randint(-50, 50))


def countSort(arr):
    min_num = min(arr)
    max_num = max(arr)
    count_list = [0]*(max_num - min_num + 1)
    for i in arr:
        count_list[i-min_num] += 1
    res = list()
    for ind, i in enumerate(count_list):
        while i != 0:
            res.append(ind + min_num)
            i -= 1
    return res


print('排序前：' + str(target))

res = countSort(target)

print('排序后：' + str(res))
