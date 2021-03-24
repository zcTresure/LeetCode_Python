# Date:       2020/12/29
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    # 贪心策略
    def minPatches(self, nums: List[int], n: int) -> int:
        count, x = 0, 1
        length, index = len(nums), 0
        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                count += 1
            print(x)
        return count


nums = list(map(int, input().split()))
n = int(input())
test = Solution()
print(test.minPatches(nums, n))
