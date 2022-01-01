# -*- coding: utf-8 -*-
# File:      1995. 统计特殊四元组.py
# DATA:      2021/12/29
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = Counter()
        for b in range(n - 3, 0, -1):
            for d in range(b + 2, n):
                cnt[nums[d] - nums[b + 1]] += 1
            for a in range(b):
                if (total := nums[a] + nums[b]) in cnt:
                    ans += cnt[total]
        return ans


nums = [3, 3, 6, 4, 5]
print(Solution().countQuadruplets(nums))
