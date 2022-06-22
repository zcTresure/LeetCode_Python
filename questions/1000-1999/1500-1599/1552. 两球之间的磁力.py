# -*- coding: utf-8 -*-
# File:      1552. 两球之间的磁力.py
# DATA:      2022/6/22
# Software:  PyCharm
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(x: int) -> int:
            pre = position[0]
            cnt = 1
            for i in range(1, len(position)):
                if position[i] - pre >= x:
                    cnt += 1
                    pre = position[i]
            return cnt

        ans = 0
        position.sort()
        left, right = 1, position[-1]
        while left <= right:
            mid = (right + left) // 2
            if check(mid) >= m:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


print(Solution().maxDistance(position=[1, 2, 3, 4, 5, 6], m=3))
