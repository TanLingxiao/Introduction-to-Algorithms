import random
import math


n = 20
target = []
for _ in range(n):
    target.append(random.randint(-50, 50))


def build_max_heap(arr):
    for i in range(math.floor(len(arr)/2), -1, -1):  # 构建堆由下往上构建所以用-1
        heapify(arr, i)


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heap_sort(arr):
    global arrLen
    arrLen = len(arr)
    build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1  # 每次剔除最大值
        heapify(arr, 0)
    return arr


print("原始数组：" + str(target))
arr = heap_sort(target)
print('堆排序后： ' + str(arr))
