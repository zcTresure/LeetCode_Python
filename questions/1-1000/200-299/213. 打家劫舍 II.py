# File Name:  213. 打家劫舍 II
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2, end):
                first, second = second, max(first + nums[i], second)
            return second

        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)
        else:
            return max(robRange(0, length - 1), robRange(1, length))


nums = [2, 3, 2]
test = Solution()
print(test.rob(nums))
