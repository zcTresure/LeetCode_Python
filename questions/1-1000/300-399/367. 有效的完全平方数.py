# -*- coding: utf-8 -*-
# File:      367. 有效的完全平方数.py
# DATA:      2021/11/4
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 二分查找
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (right - left) // 2 + left
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

    # 牛顿迭代法
    def isPerfectSquare(self, num: int) -> bool:
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            if x0 - x1 < 1e-6:
                break
            x0 = x1
        x0 = int(x0)
        return x0 * x0 == num


if __name__ == '__main__':
    num = 4
    print(Solution().isPerfectSquare(num))
