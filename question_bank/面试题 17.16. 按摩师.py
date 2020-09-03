class Solution:
    def massage(self, nums: list) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, n):
            dp[i] = max(nums[i] + max(dp[i - 2], dp[i - 3]), dp[i])
            print(dp)
        return max(dp)


class Solution:
    def massage(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tdp0 = max(dp0, dp1)   # 计算 dp[i][0]
            tdp1 = dp0 + nums[i]   # 计算 dp[i][1]
            dp0, dp1 = tdp0, tdp1
        return max(dp0, dp1)


nums = [1, 2, 3, 1]
print(Solution.massage(1, nums))
