# -*- coding: utf-8 -*-
# File:      46. 全排列.py
# DATA:      2021/12/18
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


nums = [1, 2, 3]
print(Solution().permute(nums))
