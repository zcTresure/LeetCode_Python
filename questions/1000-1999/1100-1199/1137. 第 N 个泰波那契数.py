# -*- coding: utf-8 -*-
# File:      1137. 第 N 个泰波那契数.py
# DATA:      2021/8/8
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    @classmethod
    def tribonacci(self, n: int) -> int:
        t1, t2, t3 = 0, 1, 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            tmp = 0
            for i in range(3, n + 1):
                t1, t2, t3 = t2, t3, t1 + t2 + t3
            return t3

    @classmethod
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        def multiply(a: List[List[int]], b: List[List]) -> List[List[int]]:
            c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(3):
                for j in range(3):
                    c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j] + a[i][2] * b[2][j]
            return c

        def matrix_pow(a: List[List[int]], n: int) -> List[List[int]]:
            res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            while n > 0:
                if n & 1:
                    res = multiply(res, a)
                n >>= 1
                a = multiply(a, a)
            return res

        q = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        res = matrix_pow(q, n)
        return res[0][2]


print(Solution.tribonacci(25))
