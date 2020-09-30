class Solution:
    # 暴力
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

    # 暴力 优化
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums) - 1):
            subNums = nums[i + 1:]
            if (target - nums[i]) in subNums:
                return [i, i + subNums.index(target - nums[i]) + 1]

    # 哈希表
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        for i, num in enumerate(nums):
            j = hashmap.get(target - num) 
            if j != None and i != j:
                return [i, j]

    # 哈希表 优化
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i


nums = [1, 4, 1, 4, 15]
target = 8
test = Solution()
print(test.twoSum(nums, target))
