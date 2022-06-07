# -*- coding: utf-8 -*-
# File:      875. 爱吃香蕉的珂珂.py
# DATA:      2022/6/7
# Software:  PyCharm
__author__ = 'zcFang'

from bisect import bisect_left
from math import ceil
from typing import List


class Solution:
    # 顺序查找，时间超限
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        speed = max(total // h, 1)
        while True:
            cnt = 0
            for pile in piles:
                cnt += ceil(pile / speed)
                # print(pile, speed, cnt)
            if cnt > h:
                speed += 1
            else:
                break
        return speed

    # 二分查找
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     # python3.1版本bisect_left 有key 参数，3.1以上版本不支持key参数
    #     return bisect_left(range(max(piles)), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
