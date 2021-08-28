from typing import List
from itertools import accumulate


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))


nums = [1, 2, 3, 4, 5]
test = Solution()
print(test.runningSum(nums))
