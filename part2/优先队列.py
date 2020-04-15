import random
import math
# 基于堆实现


class PriorityQueue():
    def __init__(self, arr):
        self.arr = arr
        self.arrLen = len(self.arr)

    def build_max_heap(self):
        for i in range(math.floor(self.arrLen/2), -1, -1):
            self.heapify(i)

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < self.arrLen and self.arr[left] > self.arr[largest]:
            largest = left
        if right < self.arrLen and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            self.swap(i, largest)
            self.heapify(largest)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.arrLen-1, 0, -1):
            self.swap(0, i)
            self.arrLen -= 1
            self.heapify(0)
        return self.arr

    def pop(self):
        return self.arr[-1]

    def push(self, v: int):
        self.arr.append(v)
        self.heap_sort()


n = 20
target = []
for _ in range(n):
    target.append(random.randint(-50, 50))
print("原始数组：" + str(target))

pq = PriorityQueue(target)
pq.heap_sort()
pq.push(1000)
print('存储数组：' + str(pq.arr))
