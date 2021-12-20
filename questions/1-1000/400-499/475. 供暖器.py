# -*- coding: utf-8 -*-
# File:      475. 供暖器.py
# DATA:      2021/12/20
# Software:  PyCharm
__author__ = 'zcFang'

from bisect import bisect_right
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect_right(heaters, house)
            i = j - 1
            rightDistance = heaters[j] - house if j < len(heaters) else float('inf')
            leftDistance = house - heaters[i] if i >= 0 else float('inf')
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans


houses = [1, 2, 3]
heaters = [2]
print(Solution().findRadius(houses, heaters))
