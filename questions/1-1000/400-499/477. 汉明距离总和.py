# -*- coding: utf-8 -*-
# File:     477. 汉明距离总和.py
# Date:     2021/5/28
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(30):
            bit_i = sum(((val >> i) & 1) for val in nums)
            ans += bit_i * (n - bit_i)
        return ans


nums = [2, 4, 14]
test = Solution()
print(test.totalHammingDistance(nums))
