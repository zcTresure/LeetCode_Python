class Solution:
    def missingNumber(self, nums):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i


nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
test = Solution()
print(test.missingNumber(nums))
