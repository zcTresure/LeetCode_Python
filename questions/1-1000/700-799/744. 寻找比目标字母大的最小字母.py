# -*- coding: utf-8 -*-
# File:      744. 寻找比目标字母大的最小字母.py
# DATA:      2022/4/3
# Software:  PyCharm
__author__ = 'zcFang'

from bisect import bisect_right
from typing import List


class Solution:
    # 顺序查找
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return next((letter for letter in letters if letter > target), letters[0])

    # 二分查找
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target)] if target < letters[-1] else letters[0]


print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="j"))
