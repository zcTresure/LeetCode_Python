# -*- coding: utf-8 -*-
# File:     1482. 制作 m 束花所需的最少天数.py
# Date:     2021/6/4
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def helper(days: int) -> bool:
            maked = flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        maked += 1
                        if maked == m:
                            break
                        flowers = 0
                else:
                    flowers = 0
            return maked == m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left


print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))
print(Solution().minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))
