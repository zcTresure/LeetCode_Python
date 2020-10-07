class Solution:
    def sortColors(self, nums: list) -> None:
        left, right, cur = 0, len(nums) - 1, 0
        while cur <= right:
            if nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            elif nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                cur += 1
                left += 1
            else:
                cur += 1


nums = [2, 0, 1]
test = Solution()
test.sortColors(nums)
print(nums)
