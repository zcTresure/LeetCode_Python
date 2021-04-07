# File Name:  81. 搜索旋转排序数组 II
# date:       2021/4/7
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        n = len(nums)
        if n == 1: return nums[0] == target
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
test = Solution()
print(test.search(nums, target))
