# File Name:  377. 组合总和 Ⅳ
# date:       2021/4/24
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]


nums = [1, 2, 3]
target = 4
test = Solution()
print(test.combinationSum4(nums, target))
