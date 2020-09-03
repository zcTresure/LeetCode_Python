class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                nums.insert(i, target)
                return i
        return len(nums)

    def searchInsert(self, nums: list, target: int) -> int:
        n = len(nums)
        left, right, ans = 0, n - 1, n
        while left <= right:
            mid = ((right - left) >> 1) + left
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


nums = [1, 3, 5, 6]
target = 5
test = Solution()
print(test.searchInsert(nums, target))
