# -*- coding: utf-8 -*-
# File:    969. 煎饼排序.py
# Date:    2022/2/19
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for n in range(len(arr), 1, -1):
            index = 0
            for i in range(n):
                if arr[i] > arr[index]:
                    index = i
            if index == n - 1:
                continue
            m = index
            for i in range((m + 1) // 2):
                arr[i], arr[m - i] = arr[m - i], arr[i]  # 原地反转
            for i in range(n // 2):
                arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]  # 原地反转
            ans.append(index + 1)
            ans.append(n)
        return ans


print(Solution().pancakeSort(arr=[3, 2, 1, 4]))

