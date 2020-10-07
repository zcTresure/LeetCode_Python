class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        while(val in nums):
            nums.pop(nums.index(val))
        return len(nums)

    def removeElement(self, nums: list, val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if(nums[i] == val):
                nums.pop(i)
        return len(nums)


nums = [3, 2, 2, 3]
val = 3
test = Solution()
print(test.removeElement(nums, val))
