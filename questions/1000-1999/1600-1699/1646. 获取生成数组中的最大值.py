# -*- coding: utf-8 -*-
# File:      1646. 获取生成数组中的最大值.py
# DATA:      2021/8/23
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + i % 2 * nums[i // 2 + 1]
        return max(nums[:n])


print(Solution().getMaximumGenerated(7))
