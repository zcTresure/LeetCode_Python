# -*- coding: utf-8 -*-
# File:      45. 跳跃游戏 II.py
# DATA:      2022/1/3
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, position = 0, len(nums) - 1
        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        return steps


nums = [2, 3, 1, 1, 4]
print(Solution().jump(nums))
