class Solution:
    # 迭代
    def findPeakElement(self, nums: list) -> int:
        return max(nums)

    # 二分查找
    def findPeakElement(self, nums: list) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (r - l) // 2 + l
            if (nums[m] > nums[m + 1]):
                r = m
            else:
                l = m + 1
        return l


nums = [1, 2, 1, 3, 5, 6, 4]
test = Solution()
print(test.findPeakElement(nums))
