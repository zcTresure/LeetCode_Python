# -*- coding: utf-8 -*-
# File:      961. 在长度 2N 的数组中找出重复 N 次的元素.py
# DATA:      2022/5/21
# Software:  PyCharm
__author__ = 'zcFang'

import random
from typing import List


class Solution:
    # 哈希表
    def repeatedNTimes(self, nums: List[int]) -> int:
        found = set()
        for num in nums:
            if num in found:
                return num
            found.add(num)
        return -1

    # 数学
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for gap in range(1, 4):
            for i in range(n - gap):
                if nums[i] == nums[i + gap]:
                    return nums[i]
        return -1

    # 随机选择
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)

        while True:
            x, y = random.randrange(n), random.randrange(n)
            if x != y and nums[x] == nums[y]:
                return nums[x]


print(Solution().repeatedNTimes(nums=[1, 2, 3, 3]))
print(Solution().repeatedNTimes(nums=[3, 3, 2, 1]))
