# -*- coding: utf-8 -*-
# File:      287. 寻找重复数.py
# DATA:      2022/6/23
# Software:  PyCharm
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


print(Solution().findDuplicate(nums=[1, 3, 4, 2, 2]))
print(Solution().findDuplicate(nums=[3, 1, 3, 4, 2]))
print(Solution().findDuplicate(nums=[1, 1, 3, 4, 2]))
