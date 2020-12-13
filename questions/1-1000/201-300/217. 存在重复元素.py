# Date:       2020/12/13
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False


nums = [1, 2, 3, 1]
test = Solution()
print(test.containsDuplicate(nums))
