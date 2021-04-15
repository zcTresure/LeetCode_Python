# File Name:  88. 合并两个有序数组
# date:       2021/4/5
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        len_1 = m + n
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[len_1 - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[len_1 - 1] = nums2[n - 1]
                n -= 1
            len_1 -= 1
        while m > 0:
            nums1[len_1 - 1] = nums1[m - 1]
            m -= 1
            len_1 -= 1
        while n > 0:
            nums1[len_1 - 1] = nums2[n - 1]
            n -= 1
            len_1 -= 1


nums1 = [1]
m = 1
nums2 = []
n = 0
test = Solution()
test.merge(nums1, m, nums2, n)
print(nums1)
