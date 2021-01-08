# Date:       2021/1/8
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        for i in range(k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
        for i in range((n - k) // 2):
            nums[k + i], nums[n - 1 - i] = nums[n - 1 - i], nums[k + i]


test = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 4
test.rotate(nums, k)
print(nums)
