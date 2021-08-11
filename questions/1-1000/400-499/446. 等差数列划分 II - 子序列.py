# -*- coding: utf-8 -*-
# File:      446. 等差数列划分 II - 子序列.py
# DATA:      2021/8/11
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class Solution:
    @classmethod
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        dic = [defaultdict(int) for _ in nums]  # 记录每个元素的等差数量
        for i, num in enumerate(nums):
            for j in range(i):
                diff = num - nums[j]  # 差值
                cnt = dic[j][diff]  # 上一个差值数量
                ans += cnt
                dic[i][diff] += cnt + 1  # 更行差值数量
        return ans


nums = [2, 4, 6, 8, 10]
print(Solution.numberOfArithmeticSlices(nums))
