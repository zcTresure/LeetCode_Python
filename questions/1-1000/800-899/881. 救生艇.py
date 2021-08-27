# -*- coding: utf-8 -*-
# File:      881. 救生艇.py
# DATA:      2021/8/26
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] > limit:
                right -= 1
            else:
                right -= 1
                left += 1
            ans += 1
        return ans


people = [3, 5, 3, 4]
limit = 5
print(Solution().numRescueBoats(people, limit))
