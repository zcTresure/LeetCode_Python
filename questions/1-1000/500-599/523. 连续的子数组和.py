# -*- coding: utf-8 -*-
# File:     523. 连续的子数组和.py
# Date:     2021/6/2
# Software: PyCharm
__author__ = 'zcFang'

from typing import List
from itertools import accumulate
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        sub_sum = [0]
        for num in nums: sub_sum.append((sub_sum[-1] + num) % k)
        dic = {}
        for idx, pre in enumerate(sub_sum):
            if pre not in dic: dic[pre] = idx
        for i in range(2, n + 1):
            if i - dic[sub_sum[i]] >= 2:
                print(i, dic[sub_sum[i]])
                return True
        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = [0] + list(accumulate(nums))
        sub_sum = set()
        for i in range(2, n + 1):
            sub_sum.add(total[i - 2] % k)
            if total[i] % k in sub_sum: return True
        return False


nums = [0, 0]
k = 1
test = Solution()
print(test.checkSubarraySum(nums, k))
