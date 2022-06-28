# -*- coding: utf-8 -*-
# File:      1630. 等差子数组.py
# DATA:      2022/6/27
# Software:  PyCharm
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(l, r):
            if r - l == 1:
                return True
            A = nums[l : r + 1]
            m = min(A)
            D = []
            for e in A:
                if e != m:
                    D.append(e - m)
            if not D:
                return True
            if len(D) != len(A) - 1:
                return False
            d = min(D)
            vis = [False] * len(D)
            for e in D:
                if e % d:
                    return False
                tmp = e // d - 1
                if tmp < 0 or tmp >= len(D) or vis[tmp]:
                    return False
                else:
                    vis[tmp] = True
            return True


        return [check(l, r) for l, r in zip(l, r)]


print(Solution().checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
