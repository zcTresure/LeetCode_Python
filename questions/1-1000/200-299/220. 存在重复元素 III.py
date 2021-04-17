# File Name:  220. 存在重复元素 III
# date:       2021/4/17
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        bucket = {}
        for i in range(len(nums)):
            tmp = nums[i] // (t + 1)
            if (tmp in bucket) or (tmp - 1 in bucket and abs(nums[i] - bucket[tmp - 1]) <= t) or \
                    (tmp + 1 in bucket and abs(nums[i] - bucket[tmp + 1]) <= t):
                return True
            bucket[tmp] = nums[i]
            if i >= k: bucket.pop(nums[i - k] // (t + 1))
        return False


nums = [1, 5, 9, 1, 5, 9]
k = 2
t = 3
test = Solution()
print(test.containsNearbyAlmostDuplicate(nums, k, t))
