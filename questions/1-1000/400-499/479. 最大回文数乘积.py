# -*- coding: utf-8 -*-
# File:      479. 最大回文数乘积.py
# DATA:      2022/4/17
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        for left in range(upper, upper // 10, -1):  # 枚举回文数的左半部分
            p, x = left, left
            while x:
                p = p * 10 + x % 10  # 翻转左半部分到其自身末尾，构造回文数 p
                x //= 10
            x = upper
            while x * x >= p:
                if p % x == 0:
                    return p % 1337
                x -= 1


print(Solution().largestPalindrome(n=2))
