# -*- coding: utf-8 -*-
# File:     421. 数组中两个数的最大异或值.py
# Date:     2021/5/16
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        L = len(bin(max(nums))) - 2  # 最大数的二进制位数越多
        for i in range(L, -1, -1):
            max_xor <<= 1
            cur_xor = max_xor | 1
            prefixes = {num >> i for num in nums}
            max_xor |= any(cur_xor ^ p in prefixes for p in prefixes)
        return max_xor


nums = [8, 10, 2]
test = Solution()
print(test.findMaximumXOR(nums))
