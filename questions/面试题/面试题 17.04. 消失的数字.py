class Solution:
    # 求和
    def missingNumber(self, nums: list) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

    # 异或
    def missingNumber(self, nums: list) -> int:
        ans = len(nums)
        for i in range(len(nums)):
            ans ^= i ^ nums[i]
        return ans


nums = [3, 0, 1]
test = Solution()
print(test.missingNumber(nums))
