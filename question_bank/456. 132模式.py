class Solution:
    def find132pattern(self, nums: list) -> bool:
        min_num = float("-inf")
        stack = []
        for num in reversed(nums):
            if min_num > num:
                return True
            while stack and stack[-1] < num:
                min_num = stack.pop()
            stack.append(num)
        return False


nums = [1, 2, 3, 4]
test = Solution()
print(test.find132pattern(nums))
