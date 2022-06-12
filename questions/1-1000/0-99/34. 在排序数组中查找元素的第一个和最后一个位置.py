# Date:       2020/12/1
# encode:      UTF-8
__author__ = "zcTresure"


class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                left = right = mid
                break
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, - 1]
        while left >= 0 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1
        return [left + 1, right - 1]

    def searchRange(self, nums: list, target: int) -> list:
        def left_fun(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        left = left_fun(nums, target)
        right = left_fun(nums, target + 1)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, right - 1]



nums = [1, 6]
target = 6
test = Solution()
print(test.searchRange(nums, target))
