# File Name:  80. 删除有序数组中的重复项 II
# date:       2021/4/6
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import Counter


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        counter = Counter(nums)
        for k, v in counter.items():
            nums[index] = k
            index += 1
            if v >= 2:
                nums[index] = k
                index += 1
        return index


nums = [0,0,1,1,1,1,2,3,3]
test = Solution()
index = test.removeDuplicates(nums)
print(nums[:index])
