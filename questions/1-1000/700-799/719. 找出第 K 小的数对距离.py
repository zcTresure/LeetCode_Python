# -*- coding: utf-8 -*-
# File:      719. 找出第 K 小的数对距离.py
# DATA:      2022/6/15
# Software:  PyCharm
from bisect import bisect_left
from typing import List


class Solution:
    # 排序 + 二分查找
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = 0
            for j, num in enumerate(nums):
                i = bisect_left(nums, num - mid, 0, j)
                cnt += j - i
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)

    # 排序 + 二分查找 + 双指针
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = i = 0
            for j, num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j - i
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)


print(Solution().smallestDistancePair(nums=[1, 3, 1], k=1))
print(Solution().smallestDistancePair(nums=[1, 3, 1], k=2))
print(Solution().smallestDistancePair(nums=[1, 6, 1], k=3))
