# -*- coding: utf-8 -*-
# File:      1502. 判断能否形成等差数列.py
# DATA:      2022/6/10
# Software:  PyCharm
from typing import List


class Solution:
    # 模拟 arr[i] - arr[i - 1] != arr[i + 1] - arr[i]
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(1, len(arr) - 1):
            if arr[i] - arr[i - 1] != arr[i + 1] - arr[i]:
                return False
        return True


print(Solution().canMakeArithmeticProgression(arr=[1, 5, 3]))
print(Solution().canMakeArithmeticProgression(arr=[1, 2, 4]))
