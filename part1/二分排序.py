target = [5, 12, 13, 28, 46, 51, 51, 65, 90, 95]


def binary_search(A: list, v: int, p: int, r: int):
    if (p > r or p == r) and v != A[p]:
        return None
    else:
        mid = int((r - p)/2) + 1
        if v == A[mid]:
            return mid
        else:
            if v < A[mid]:
                return binary_search(A, v, p, mid)
            else:
                return binary_search(A, v, mid, r)


res = binary_search(target, 13, 0, len(target)-1)
print(res)
