def cut_rod(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q


# 对应不同长度的价格表
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# 切割数量
n = 8

price = cut_rod(p, n)

print('max price is: ' + str(price))