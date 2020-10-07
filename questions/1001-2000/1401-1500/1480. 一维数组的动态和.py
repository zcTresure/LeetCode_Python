class Solution:
    def runningSum(self, nums: list) -> list:
        if not nums:
            return []
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


nums = [1, 2, 3, 4, 5]
test = Solution()
print(test.runningSum(nums))
