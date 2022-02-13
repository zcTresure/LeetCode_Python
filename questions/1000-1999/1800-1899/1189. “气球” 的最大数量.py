# -*- coding: utf-8 -*-
# File:    1189. “气球” 的最大数量.py
# Date:    2022/2/13
# Software: Pycharm
__author__ = 'zcFang'

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(c for c in text if c in 'balon')
        count['l'] //= 2
        count['o'] //= 2
        return min(count.values()) if len(count) == 5 else 0


print(Solution().maxNumberOfBalloons(text="balloon"))
