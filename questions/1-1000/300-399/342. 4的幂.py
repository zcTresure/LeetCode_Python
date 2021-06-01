# -*- coding: utf-8 -*-
# File:     342. 4的幂.py
# Date:     2021/5/31
# Software: PyCharm
__author__ = 'zcFang'


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0


n = int(input())
test = Solution()
print(test.isPowerOfFour(n))
