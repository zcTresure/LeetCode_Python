class Solution:
    # 二分查找
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = (h + l) >> 1
            if nums[m] < nums[h]:
                h = m
            elif nums[m] > nums[h]:
                l = m + 1
            else:
                h -= 1
        return nums[l]
