# -*- coding: utf-8 -*-
# File:      581. 最短无序连续子数组.py
# DATA:      2021/8/3
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        size = len(nums)
        if size <= 1:
            return 0

        left, right = size - 2, 1
        cur_min, cur_max = nums[-1], nums[0]
        up, down = 0, 1

        # 由于两个指针迭代的步数是相同的，所以没必要分两次循环，在一次循环里同时移动两次指针即可。
        while left >= 0 and right < size:
            if nums[left] > cur_min:
                down = left
            else:
                cur_min = nums[left]
            if nums[right] < cur_max:
                up = right
            else:
                cur_max = nums[right]
            left -= 1
            right += 1
        return up - down + 1


nums = [1, 3, 2, 2, 3]
test = Solution()
print(test.findUnsortedSubarray(nums))
