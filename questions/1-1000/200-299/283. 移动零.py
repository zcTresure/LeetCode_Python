

__author__ = "zcTresure"


class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                i += 1
                continue
            nums[last] = nums[i]
            last += 1
        for i in range(last, len(nums)):
            nums[i] = 0


nums = [0, 1, 0, 3, 12]
test = Solution()
test.moveZeroes(nums)
print(nums)
