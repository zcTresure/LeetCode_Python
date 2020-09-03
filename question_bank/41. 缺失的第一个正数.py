class Solution:
    def firstMissingPositive(self, nums) -> int:
        # 保证有1输出
        if 1 not in nums:
            return 1
        n = len(nums)
        # 将所有非正数和大于数组长度的数归1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        # 将所有数组元素转化为负数
        for i in range(n):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] = -nums[temp]
        # 如果第i个元素为正数 则nums[i]在原数组中为负数 且不存在abs(nums[i])
        for i in range(1, n):
            if nums[i] > 0:
                return i + 1
        # 数组元素全为正数 且nums[i] = i + 1
        return n + 1


nums = [2, 1]
test = Solution()
print(test.firstMissingPositive(nums))
