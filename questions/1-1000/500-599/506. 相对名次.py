# -*- coding: utf-8 -*-
# File:      506. 相对名次.py
# DATA:      2021/12/3
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        desc = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = [""] * len(score)
        arr = sorted(enumerate(score), key=lambda x: -x[1])
        for i, (idx, _) in enumerate(arr):
            ans[idx] = desc[i] if i < 3 else str(i + 1)
        return ans


score = [1, 2, 34, 1, 43, 2, 3]
print(Solution().findRelativeRanks(score))
