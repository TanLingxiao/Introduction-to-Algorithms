* 1.2-2 

可以看作一道数学证明题，求 $8x^2 < 64n\lg(n) \equiv  n < 8lg(n) \equiv 2^{n/8} < n$，所以n的范围应该是$[2,43]$

* 2.1-1

只需要修改代码，把每一步排序过程打印处理即可
```
原数组 [68, 69, 20, 40, 5, 57, 49, 63, 58, 57]
step 1: [68, 69, 20, 40, 5, 57, 49, 63, 58, 57]
step 2: [20, 68, 69, 40, 5, 57, 49, 63, 58, 57]
step 3: [20, 40, 68, 69, 5, 57, 49, 63, 58, 57]
step 4: [5, 20, 40, 68, 69, 57, 49, 63, 58, 57]
step 5: [5, 20, 40, 57, 68, 69, 49, 63, 58, 57]
step 6: [5, 20, 40, 49, 57, 68, 69, 63, 58, 57]
step 7: [5, 20, 40, 49, 57, 63, 68, 69, 58, 57]
step 8: [5, 20, 40, 49, 57, 58, 63, 68, 69, 57]
step 9: [5, 20, 40, 49, 57, 57, 58, 63, 68, 69]
```

* 2.1-2

将A[i] > key 条件改成 A[i] < key

* 2.1-3
```
Input: A = <a1, a2,a3....> and a value v
Output: An index i such that v = A[i] or nil if v != A
for i to n do
    if A[i] = v then
        return i
    end if
end for
return nil
```

* 2.1-4
```
Input: A and B store in nd array
Output: C store in (n+1)d array
A to a in decimal and B to b in decimal
c = a + b
c to C in binary and store in (n+1)d array
```

* 2.2-1 

$\Theta(n^3)$ 

* 2.2-2
```
Input: A = <a1, a2, a3.....>
Output: sorted A
for i = 1 to n - 1 do
    index j = FIND-MIN(A,i,n)
    swap A[j] A[i]
end for
```
循环不变式：A[1 to i - 1]

只需要针对n-1个元素的原因是第n个元素永远是最大的

最好最坏时间都是$\Theta(n^2)$ 

* 2.2-3

最好最坏时间是$\Theta(n)$ 

* 2.2-4

可以通过修改使算法专门处理有效的最佳输入以使其具有最佳情况的运行时间。