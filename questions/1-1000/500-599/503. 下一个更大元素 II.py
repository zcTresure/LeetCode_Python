# Date:       2021/3/6
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    # 单调栈
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n * 2 - 1):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return res


nums = [1, 2, 1]
test = Solution()
print(test.nextGreaterElements(nums))
