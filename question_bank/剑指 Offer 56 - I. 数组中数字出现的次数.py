import functools


class Solution:
    def singleNumbers(self, nums: list) -> list:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret:
            div <<= 1
        a, b = 0, 0
        for num in nums:
            if num & div:
                a ^= num
            else:
                b ^= num
        return [a, b]


nums = [4, 1, 4, 6]
test = Solution()
print(test.singleNumbers(nums))
