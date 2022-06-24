# -*- coding: utf-8 -*-
# File:      1870. 准时到达的列车最小时速.py
# DATA:      2022/6/24
# Software:  PyCharm
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        hr = round(hour * 100)
        # 时间必须要大于路程段数减 1
        if hr <= 100 * (n - 1):
            return -1

        # 判断当前时速是否满足时限
        def check(speed: int) -> bool:
            t = 0
            # 前 n-1 段中第 i 段贡献的时间： floor(dist[i] / mid)
            for i in range(n - 1):
                t += (dist[i] - 1) // speed + 1
            # 最后一段贡献的时间： dist[n-1] / mid
            t *= speed
            t += dist[-1]
            return t * 100 <= hr * speed  # 通分以转化为整数比较

        # 二分
        l, r = 1, 10 ** 7
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l  # 满足条件的最小时速


print(Solution().minSpeedOnTime(dist=[1, 3, 2], hour=6))
