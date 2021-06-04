# -*- coding: utf-8 -*-
# File:     1482. 制作 m 束花所需的最少天数.py
# Date:     2021/6/4
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m > len(bloomDay) / k:
            return -1

        def canMake(days: int) -> bool:
            bouquets = flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        if bouquets == m:
                            break
                        flowers = 0
                else:
                    flowers = 0
            return bouquets == m

        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            days = (low + high) // 2
            if canMake(days):
                high = days
            else:
                low = days + 1
        return low


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
print(Solution().minDays(bloomDay, m, k))
