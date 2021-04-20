# File Name:  26. 删除排序数组中的重复项
# date:       2020/9/29
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        a, b = 0, 1
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
