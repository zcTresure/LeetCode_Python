class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        res = tmp = 0
        for num in nums:
            if num:
                tmp += 1
            else:
                res = max(res, tmp)
                tmp = 0
        res = max(res, tmp)
        return res

    def findMaxConsecutiveOnes(self, nums: list) -> int:
        res = tmp = 0
        for num in nums:
            res = max(res, tmp)
            tmp += 1 if num else -tmp

        res = max(res, tmp)
        return res


nums = [1, 1, 0, 1, 1, 1]
test = Solution()
print(test.findMaxConsecutiveOnes(nums))
