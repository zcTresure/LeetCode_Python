class Solution:
    def removeDuplicates(self, nums: list) -> int:
        a = 0
        b = 1
        while b < len(nums):
            if nums[b] == nums[a]:
                b += 1
            else:
                a += 1
                nums[a] = nums[b]
        return a + 1


nums = [1, 1, 2]
test = Solution()
print(test.removeDuplicates(nums))
