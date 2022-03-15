# -*- coding: utf-8 -*-
# File:      599. 两个列表的最小索引总和.py
# DATA:      2022/3/14
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {s: i for i, s in enumerate(list1)}
        ans = []
        index_sum = float('inf')
        for i, s in enumerate(list2):
            if s in index:
                j = index[s]
                if i + j < index_sum:
                    index_sum = i + j
                    ans = [s]
                elif i + j == index_sum:
                    ans.append(s)
        return ans


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(Solution().findRestaurant(list1, list2))
