# -*- coding: utf-8 -*-
# File:      398. 随机数索引.py
# DATA:      2022/4/25
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from random import choice, randrange
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for i, num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.pos[target])


class Solution1:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1  # 第 cnt 次遇到 target
                if randrange(cnt) == 0:
                    ans = i
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
