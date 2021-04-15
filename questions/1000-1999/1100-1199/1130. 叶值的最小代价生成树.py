# File Name:  1130. 叶值的最小代价生成树
# date:       2021/4/14
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from functools import lru_cache


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i + 1 == j:  # leaf
                return 0
            final_score = float('Inf')
            for k in range(i + 1, j):
                left_score, right_score = dp(i, k), dp(k, j)
                left_max, right_max = max(arr[i:k]), max(arr[k:j])
                final_score = min(final_score, left_score + right_score + left_max * right_max)
            return final_score

        return dp(0, len(arr))


nums = [6, 2, 4]
test = Solution()
print(test.mctFromLeafValues(nums))
