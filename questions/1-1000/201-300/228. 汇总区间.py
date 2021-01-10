# Date:       2021/1/10
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = list()
        index = 0
        while index < n:
            pre = index
            index += 1
            # 判断是否为最小有序
            while index < n and nums[index - 1] == nums[index] - 1:
                index += 1
            cur = index - 1
            if pre < cur:  # 区间有多个元素
                ans.append(str(nums[pre]) + '->' + str(nums[cur]))
            else:  # 区间只有一个元素
                ans.append(str(nums[pre]))
        return ans


nums = []
test = Solution()
print(test.summaryRanges(nums))
