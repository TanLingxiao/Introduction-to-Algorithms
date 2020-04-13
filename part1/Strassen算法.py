import numpy as np


def mergeMatrix(A11, A12, A13, A14):
    n = len(A11)
    for i in range(0, n):
        A11[i].extend(A12[i])
        A13[i].extend(A14[i])
    for i in range(0, n):
        A11.append(A13[i])
    return A11


def division(matrix):
    A11 = []
    A12 = []
    A21 = []
    A22 = []
    half_size = int(len(matrix) / 2)
    for i in range(0, half_size):
        A11.append(matrix[i][:half_size])
        A12.append(matrix[i][half_size:])
    for j in range(half_size, len(matrix)):
        A21.append(matrix[j][:half_size])
        A22.append(matrix[j][half_size:])
    return A11, A12, A21, A22


class Strassen:
    def add(self, m1, m2, size):
        matrix = []
        for i in range(0, size):
            temp = []
            for j in range(0, size):
                temp.append(m1[i][j] + m2[i][j])
            matrix.append(temp)
        return matrix

    def sub(self, m1, m2, size):
        matrix = []
        for i in range(0, size):
            temp = []
            for j in range(0, size):
                temp.append(m1[i][j] - m2[i][j])
            matrix.append(temp)
        return matrix

    def multiply(self, m1, m2, size):
        if(size == 1):
            return [[m1[0][0] * m2[0][0]]]
        A11, A12, A21, A22 = division(m1)
        B11, B12, B21, B22 = division(m2)
        size = int(size / 2)
        m1 = self.multiply(A11, self.sub(B12, B22, size), size)
        m2 = self.multiply(self.add(A11, A12, size), B22, size)
        m3 = self.multiply(self.add(A21, A22, size), B11, size)
        m4 = self.multiply(A22, self.sub(B21, B11, size), size)
        m5 = self.multiply(self.add(A11, A22, size),
                           self.add(B11, B22, size), size)
        m6 = self.multiply(self.sub(A12, A22, size),
                           self.add(B21, B22, size), size)
        m7 = self.multiply(self.sub(A11, A21, size),
                           self.add(B11, B12, size), size)
        C11 = self.add(self.sub(self.add(m5, m4, size), m2, size), m6, size)
        C12 = self.add(m1, m2, size)
        C21 = self.add(m3, m4, size)
        C22 = self.sub(self.sub(self.add(m5, m1, size), m3, size), m7, size)
        return mergeMatrix(C11, C12, C21, C22)


s = Strassen()

N = 5  # 随机数组维度

matrixA = np.random.randint(-10, 10, (N, N))
matrixB = np.random.randint(-10, 10, (N, N))
print(matrixA)
print(matrixB)
print(s.multiply(matrixA, matrixB, N))
