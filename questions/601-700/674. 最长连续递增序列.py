class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        n = len(nums)
        if not nums or n < 0:
            return 0
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)


nums = [2, 2, 2, 2, 2]
test = Solution()
print(test.findLengthOfLCIS(nums))
