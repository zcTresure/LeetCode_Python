import math


class Solution:
    def findNumbers(self, nums: list) -> int:
        ans, length = 0, 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ans += 1
        return ans

    def findNumbers(self, nums: list) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)

    def findNumbers(self, nums: list) -> int:
        return sum(1 for num in nums if int(math.log10(num) + 1) % 2 == 0)


nums = [12, 345, 2, 6, 7896]
test = Solution()
print(test.findNumbers(nums))
