# -*- coding: utf-8 -*-
# File:      532. 数组中的 k-diff 数对.py
# DATA:      2022/6/16
# Software:  PyCharm

from typing import List


class Solution:
    # 哈希表
    def findPairs(self, nums: List[int], k: int) -> int:
        visited, ans = set(), set()
        for num in nums:
            if num - k in visited:
                ans.add(num - k)
            if num + k in visited:
                ans.add(num)
            visited.add(num)
        return len(ans)

    # 排序 + 双指针
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n, y, res = len(nums), 0, 0
        for x in range(n):
            if x == 0 or nums[x] != nums[x - 1]:
                while y < n and (nums[y] < nums[x] + k or y <= x):
                    y += 1
                if y < n and nums[y] == nums[x] + k:
                    res += 1
        return res


print(Solution().findPairs(nums=[1, 2, 3, 4, 5], k=1))
