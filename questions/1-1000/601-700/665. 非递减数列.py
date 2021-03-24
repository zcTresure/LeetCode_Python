# Date:       2021/2/8
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(n - 1):
            x, y = nums[i], nums[i + 1]
            if x > y:
                cnt += 1
                if cnt > 1:
                    return False
                if i > 0 and y < nums[i - 1]:
                    nums[i + 1] = x
        return True


test = Solution()
nums = [4, 2, 1]
print(test.checkPossibility(nums))
