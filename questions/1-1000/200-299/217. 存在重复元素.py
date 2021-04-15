# Date:       2020/12/13
# encode:      UTF-8
__author__ = "zcTresure"


class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

    def containsDuplicate(self, nums: list) -> bool:
        return len(set(nums)) < len(nums)


nums = [1, 2, 3]
test = Solution()
print(test.containsDuplicate(nums))
