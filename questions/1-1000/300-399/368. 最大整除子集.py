# File Name:  368. 最大整除子集
# date:       2021/4/23
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        result = []
        max_size, max_val = 1, dp[0]
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_size:
                max_size = dp[i]
                max_val = nums[i]
        if max_size == 1:
            return [nums[0]]
        for i in range(n - 1, -1, -1):
            if max_size > 0 and dp[i] == max_size and max_val % nums[i] == 0:
                result.append(nums[i])
                max_size -= 1
                max_val = nums[i]
        return result


nums = [1, 2, 4, 8]
test = Solution()
print(test.largestDivisibleSubset(nums))
