class Solution:
    # 排序
    def missingNumber(self, nums: list) -> int:
        nums.sort()
        for index, ele in enumerate(nums):
            if index != ele:
                return index
        return len(nums)
    # 哈希表
    def missingNumber(self, nums: list) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
    # 位运算
    def missingNumber(self, nums: list) -> int:
        miss = len(nums)
        for i, num in enumerate(nums):
            miss ^= i ^ num
        return miss
    # 数学
    def missingNumber(self, nums: list) -> int:
        n = len(nums)
        return (((n + 1) * n) // 2) - sum(nums)


nums = [0, 1, 3]
test = Solution()
print(test.missingNumber(nums))
