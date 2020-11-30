# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "zcTresure"


class Solution:
    def reversePairsRecursive(self, nums: list, left: int, right: int):
        if left == right:
            return 0
        mid = (left + right) >> 1
        n1 = self.reversePairsRecursive(nums, left, mid)
        n2 = self.reversePairsRecursive(nums, mid + 1, right)
        res = n1 + n2
        i, j = left, mid + 1
        # 统计下标对数量
        while i <= mid:
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            res += (j - mid - 1)
            i += 1
        tmp = [0] * (right - left + 1)
        p1, p2, p = left, mid + 1, 0
        # 合并两个排序数组
        while p1 <= mid or p2 <= right:
            if p1 > mid:
                tmp[p] = nums[p2]
                p2 += 1
            elif p2 > right:
                tmp[p] = nums[p1]
                p1 += 1
            else:
                if nums[p1] < nums[p2]:
                    tmp[p] = nums[p1]
                    p1 += 1
                else:
                    tmp[p] = nums[p2]
                    p2 += 1
            p += 1
        for i in range(len(tmp)):
            nums[left + i] = tmp[i]
        return res

    def reversePairs(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        return self.reversePairsRecursive(nums, 0, len(nums) - 1)


nums = [1, 3, 2, 3, 1]
test = Solution()
print(test.reversePairs(nums))
