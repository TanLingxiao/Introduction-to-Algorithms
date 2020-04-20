import random


n = 20
target = []
for _ in range(n):
    target.append(random.randint(0, 200))


def countingSort(arr, exp):

    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i]/exp
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = arr[i]/exp
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max_num = max(arr)
    exp = 1
    while max_num/exp > 0:
        countingSort(arr, exp)
        exp *= 10


print('排序前：' + str(target))

radixSort(target)

print('排序后：' + str(target))
