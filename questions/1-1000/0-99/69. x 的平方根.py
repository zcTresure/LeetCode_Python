# -*- coding: utf-8 -*-
# File:      69. x 的平方根.py
# DATA:      2022/6/1
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        for i in range(1, x + 1):
            if i * i >= x:
                if i * i == x:
                    return i
                else:
                    return i - 1

    # 二分查找
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, -1
        while left <= right:
            mid = (right - left) // 2 + left
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C  / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


print(Solution().mySqrt(4))
