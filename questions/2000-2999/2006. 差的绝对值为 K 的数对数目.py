# -*- coding: utf-8 -*-
# File:    2006. 差的绝对值为 K 的数对数目.py
# Date:    2022/2/13
# Software: Pycharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans

    def countKDifference(self, nums: List[int], k: int) -> int:
        res, count = 0, Counter()
        for num in nums:
            res += count[num - k] + count[num + k]
            count[num]+=1
        return res


print(Solution().countKDifference(nums=[1, 2, 2, 1], k=1))
