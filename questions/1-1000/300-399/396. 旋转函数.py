# -*- coding: utf-8 -*-
# File:      396. 旋转函数.py
# DATA:      2022/4/22
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
        return res


print(Solution().maxRotateFunction(nums=[4, 3, 2, 6]))
