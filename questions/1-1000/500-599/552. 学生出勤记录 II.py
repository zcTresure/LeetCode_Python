# -*- coding: utf-8 -*-
# File:      552. 学生出勤记录 II.py
# DATA:      2021/8/18
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 动态规划
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # 长度，A的数量，结尾L的数量
        dp = [[0, 0, 0], [0, 0, 0]]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp_new = [[0, 0, 0], [0, 0, 0]]

            # 以P结尾的数量
            for j in range(0, 2):
                for k in range(0, 3):
                    dp_new[j][0] = (dp_new[j][0] + dp[j][k]) % MOD

            # 以A结尾的数量
            for k in range(0, 3):
                dp_new[1][0] = (dp_new[1][0] + dp[0][k]) % MOD

            # 以L结尾的数量
            for j in range(0, 2):
                for k in range(1, 3):
                    dp_new[j][k] = (dp_new[j][k] + dp[j][k - 1]) % MOD

            dp = dp_new
        total = 0
        for j in range(0, 2):
            for k in range(0, 3):
                total += dp[j][k]
        return total % MOD

    # 矩阵快速幂
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        mat = [[1, 1, 0, 1, 0, 0],
               [1, 0, 1, 1, 0, 0],
               [1, 0, 0, 1, 0, 0],
               [0, 0, 0, 1, 1, 0],
               [0, 0, 0, 1, 0, 1],
               [0, 0, 0, 1, 0, 0], ]

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            rows, columns, temp = len(a), len(b[0]), len(b)
            c = [[0] * columns for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    for k in range(temp):
                        c[i][j] += a[i][k] * b[k][j]
                        c[i][j] %= MOD
            return c

        def matrixPow(mat: List[List[int]], n: int) -> List[List[int]]:
            ret = [[1, 0, 0, 0, 0, 0]]
            while n > 0:
                if (n & 1) == 1:
                    ret = multiply(ret, mat)
                n >>= 1
                mat = multiply(mat, mat)
            return ret

        res = matrixPow(mat, n)
        ans = sum(res[0])
        return ans % MOD


print(Solution().checkRecord(2))
