# -*- coding: utf-8 -*-
# File:    1748. 唯一元素的和.py
# Date:    2022/2/13
# Software: Pycharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num, val in Counter(nums).items() if val == 1)


print(Solution().sumOfUnique(nums=[1, 2, 3, 4, 2, 3, 2]))
