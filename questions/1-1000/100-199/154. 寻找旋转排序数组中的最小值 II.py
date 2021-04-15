# File Name:  154. 寻找旋转排序数组中的最小值 II
# date:       2021/4/9
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = right - 1
        return nums[left]


nums = [1, 3, 5]
test = Solution()
print(test.findMin(nums))
