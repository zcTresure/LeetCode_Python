class Solution:
    # 二分查找
    def findMin(self, nums: list) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


nums = [3, 4, 5, 1, 2]
test = Solution()
print(test.findMin(nums))
