# -*- coding: utf-8 -*-
# File:      1822. 数组元素积的符号.py
# DATA:      2022/6/10
# Software:  PyCharm
from functools import reduce
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        if 0 in nums: return 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                ans *= -1
        return ans


print(Solution().arraySign(nums=[-1, -2, -3, -4, 3, 2, 1]))
print(Solution().arraySign(nums=[1, 5, 0, 2, -3]))
print(Solution().arraySign(nums=[-1, 1, -1, 1, -1]))
