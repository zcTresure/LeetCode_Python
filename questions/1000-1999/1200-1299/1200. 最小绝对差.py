# -*- coding: utf-8 -*-
# File:    1200. 最小绝对差.py
# Date:    2022/7/4
# Software: Pycharm
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_sub = float('inf')
        for i in range(1, len(arr)):
            sub = arr[i] - arr[i - 1]
            if sub == min_sub:
                ans.append([arr[i - 1], arr[i]])
            elif sub < min_sub:
                ans = [[arr[i - 1], arr[i]]]
                min_sub = sub
        return ans


print(Solution().minimumAbsDifference(arr=[4, 3, 1, 2]))
print(Solution().minimumAbsDifference(arr=[1, 3, 6, 10, 15]))
print(Solution().minimumAbsDifference(arr=[3, 8, -10, 23, 19, -4, -14, 27]))
