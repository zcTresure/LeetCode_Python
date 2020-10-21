class Solution:
    def majorityElement(self, nums: list) -> int:
        ans, count = float('inf'), 0
        for num in nums:
            if num == ans:
                count += 1
            elif count > 0:
                count -= 1
            else:
                ans = num
        count = 0
        for num in nums:
            if num == ans:
                count += 1
        if count * 2 > len(nums):
            return ans
        else:
            return -1


nums = [2, 2, 1, 1, 1, 2, 2]
test = Solution()
print(test.majorityElement(nums))
