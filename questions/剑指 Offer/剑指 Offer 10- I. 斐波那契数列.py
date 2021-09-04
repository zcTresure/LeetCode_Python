# -*- coding: utf-8 -*-
# File:      剑指 Offer 10- I. 斐波那契数列.py
# DATA:      2021/9/4
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 动态规划
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b, c = 0, 0, 1
        MOD = 10 ** 9 + 7
        for i in range(2, n + 1):
            a = b
            b = c
            c = (a + b) % MOD
        return c

    # 矩阵快速幂
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        MOD = 10 ** 9 + 7

        def muptiply(a: list, b: list) -> list:
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
            return c

        def matrix_pow(a: list, n: int) -> list:
            ret = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1:
                    ret = muptiply(ret, a)
                n >>= 1
                a = muptiply(a, a)
            return ret

        res = matrix_pow([[1, 1], [1, 0]], n - 1)
        return res[0][0]


n = 10
print(Solution().fib(n))
