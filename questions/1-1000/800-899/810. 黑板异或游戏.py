# -*- coding: utf-8 -*-
# File:     810. 黑板异或游戏.py
# Date:     2021/5/22
# Software: PyCharm
__author__ = 'zcFang'

from functools import reduce
from operator import xor
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return reduce(xor, nums) == 0 or len(nums) % 2 == 0


nums = [1, 1, 2]
test = Solution()
print(test.xorGame(nums))
