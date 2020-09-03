class Solution:
    def maxSubArray(self, nums: list) -> int:
        n = len(nums)
        dp = [-float('inf')] * (n + 1)
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        print(dp)
        return max(dp)


nums = [-2]
print(Solution.maxSubArray(1, nums))
