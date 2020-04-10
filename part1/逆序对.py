from typing import List

# 改造归并排序，统计排序过程中的交换次数

target = [2, 3, 8, 6, 1]

count = 0


def reversePairs(nums: List[int]) -> int:
    def merge(A, B):
        n1, n2 = len(A), len(B)
        i, j = 0, 0
        C = []
        count = 0
        while i < n1 and j < n2:
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                # 计算一次即可
                count += (n1-i)
                j += 1
        if i < n1:
            C += A[i:]
        if j < n2:
            C += B[j:]
        return C, count

    def mergesort(nums, left, right):
        if left >= right:
            return nums[left:right+1], 0
        mid = left + (right-left)//2
        A, n1 = mergesort(nums, left, mid)
        B, n2 = mergesort(nums, mid+1, right)
        C, n3 = merge(A, B)
        return C, n1+n2+n3

    A, res = mergesort(nums, 0, len(nums)-1)
    return res


res = reversePairs(target)
print(res)
