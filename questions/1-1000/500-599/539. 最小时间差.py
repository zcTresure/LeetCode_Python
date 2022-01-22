# -*- coding: utf-8 -*-
# File:    539. 最小时间差.py
# Date:    2022/1/18
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


def getMinutes(t: str) -> int:
    return ((ord(t[0]) - ord('0')) * 10 + ord(t[1]) - ord('0')) * 60 + (ord(t[3]) - ord('0')) * 10 + ord(t[4]) - ord(
        '0')


class Solution:
    # 排序
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = float('inf')
        t0Minutes = getMinutes(timePoints[0])
        preMinutes = t0Minutes
        for i in range(1, len(timePoints)):
            minutes = getMinutes(timePoints[i])
            ans = min(ans, minutes - preMinutes)  # 相邻时间的时间差
            preMinutes = minutes
        ans = min(ans, t0Minutes + 1440 - preMinutes)  # 首尾时间的时间差
        return ans

    # 鸽巢原理
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        if n > 1440:
            return 0
        timePoints.sort()
        ans = float('inf')
        t0Minutes = getMinutes(timePoints[0])
        preMinutes = t0Minutes
        for i in range(1, n):
            minutes = getMinutes(timePoints[i])
            ans = min(ans, minutes - preMinutes)  # 相邻时间的时间差
            preMinutes = minutes
        ans = min(ans, t0Minutes + 1440 - preMinutes)  # 首尾时间的时间差
        return ans


print(Solution().findMinDifference(timePoints=["00:00", "23:59", "00:00"]))
