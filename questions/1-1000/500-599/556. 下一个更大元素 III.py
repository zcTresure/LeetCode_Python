# -*- coding: utf-8 -*-
# File:      556. 下一个更大元素 III.py
# DATA:      2022/6/28
# Software:  PyCharm
class Solution:
    def nextGreaterElement(self, num: int) -> int:
        nums = []
        while num:
            nums.append(num % 10)
            num //= 10
        nums = nums[::-1]

        # 倒着找到第一个减少的数字
        i = len(nums) - 1
        while i == len(nums) - 1 or (i >= 0 and nums[i] >= nums[i + 1]):
            i -= 1

        if i < 0:
            return -1

        # 找到第一个比val大的数字，并交换
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        # i后面的数字逆序
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # 重新组合
        MAX_INT = 2 ** 31 - 1
        MAX_VAL, MAX_MOD = MAX_INT // 10, MAX_INT % 10
        res = 0
        for i in range(len(nums)):
            if res > MAX_VAL or (res == MAX_VAL and nums[i] > MAX_MOD):
                return -1
            res = res * 10 + nums[i]
        return res


print(Solution().nextGreaterElement(num=12))
print(Solution().nextGreaterElement(num=21))
print(Solution().nextGreaterElement(num=1234))
