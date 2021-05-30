# -*- coding: utf-8 -*-
# File:     231. 2 的幂.py
# Date:     2021/5/30
# Software: PyCharm
__author__ = 'zcFang'


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


n = 8
test = Solution()
print(test.isPowerOfTwo(n))
