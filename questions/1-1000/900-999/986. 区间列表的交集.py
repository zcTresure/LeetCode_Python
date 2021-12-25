# -*- coding: utf-8 -*-
# File:    986. 区间列表的交集.py
# Date:    2021/12/25
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            if low <= high:
                ans.append([low, high])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(Solution().intervalIntersection(firstList, secondList))
