from functools import reduce
from collections import Counter


class Solution:
    # 暴力查找
    def singleNumber(self, nums: list) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            flag = True
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    flag = False
                    break
            if flag:
                return nums[i]
        return nums[len(nums) - 1]

    # 排序
    def singleNumber(self, nums: list) -> int:
        if not nums:
            return -1
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[len(nums) - 1]

    # 字典计数
    def singleNumber(self, nums: list) -> int:
        datas = Counter(nums)
        for each in datas:
            if datas[each] == 1:
                return each

    # 集合去重后求和
    def singleNumber(self, nums: list) -> int:
        return sum(set(nums)) * 2 - sum(nums)

    # 异或
    def singleNumber(self, nums: list) -> int:
        for i in range(len(nums)):
            if i == 0:
                res = nums[i]
            else:
                res ^= nums[i]
        return res

    # 异或 + reduce函数
    def singleNumber(self, nums: list) -> int:
        return reduce(lambda x, y: x ^ y, nums)


nums = [4, 1, 2, 1, 2, 4, 3]
test = Solution()
print(test.singleNumber(nums))
