# -*- coding: utf-8 -*-
# File:      1760. 袋子里最少数目的球.py
# DATA:      2022/6/21
# Software:  PyCharm
from collections import Counter
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        counter = Counter(nums)
        while maxOperations:
            max_key = max(counter.keys())
            counter[max_key] -= 1
            if counter[max_key] == 0:
                counter.pop(max_key)
            tmp = max_key // 2
            counter[tmp if max_key % 2 == 0 else tmp + 1] += 1
            counter[tmp] += 1
            maxOperations -= 1
            print(max_key, counter)
        return max(counter.keys())

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # x是每个袋子最多装的球个数，返回拆分次数
        def operates(x: int) -> int:
            oper = 0
            for num in nums:
                if num > x:
                    oper += (num - 1) // x
            return oper

        left, right = 1, max(nums)
        if operates(left) == maxOperations:
            return left
        while left < right:
            mid = (left + right) // 2
            if operates(mid) <= maxOperations:
                right = mid
            else:
                left = mid + 1
        return left


print(Solution().minimumSize(nums=[9], maxOperations=2))
print(Solution().minimumSize(nums=[2, 4, 8, 2], maxOperations=4))
print(Solution().minimumSize(nums=[7, 17], maxOperations=2))
