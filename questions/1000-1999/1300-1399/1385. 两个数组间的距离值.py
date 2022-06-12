# -*- coding: utf-8 -*-
# File:      1385. 两个数组间的距离值.py
# DATA:      2022/6/10
# Software:  PyCharm
from bisect import bisect_left
from typing import List


class Solution:
    # 模拟
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                cnt += 1
        return cnt

    # 二分查找
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for x in arr1:
            p = bisect_left(arr2, x)
            if p == len(arr2) or abs(x - arr2[p]) > d:
                if p == 0 or abs(x - arr2[p - 1]) > d:
                    cnt += 1
        return cnt


print(Solution().findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
