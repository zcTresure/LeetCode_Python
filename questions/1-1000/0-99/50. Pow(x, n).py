# -*- coding: utf-8 -*-
# File:      50. Pow(x, n).py
# DATA:      2021/10/12
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 快速幂递归
    def myPow(self, x: float, n: int) -> float:
        def quickMul(n: int) -> float:
            if n == 0:
                return 1.0
            y = quickMul(n // 2)
            return y * y if n % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    # 快速幂迭代
    def myPow(self, x: float, n: int) -> float:
        def quickMul(x: float, n: int) -> float:
            ans = 1.0
            while n > 0:
                if n % 2 == 1:
                    ans *= x
                x *= x
                n //= 2
            return ans

        return quickMul(x, n) if n >= 0 else 1.0 / quickMul(x, -n)


print(Solution().myPow(2, 31))
