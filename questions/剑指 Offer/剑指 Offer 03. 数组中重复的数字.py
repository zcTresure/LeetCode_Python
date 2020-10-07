class Solution:
    # 字典查重
    def findRepeatNumber(self, nums: list) -> int:
        if not nums:
            return -1
        count = set()
        for num in nums:
            if num not in count:
                count.add(num)
            else:
                return num
        return -1

    # 排序
    def findRepeatNumber(self, nums: list) -> int:
        if not nums:
            return -1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return -1

    # 桶排序
    def findRepeatNumber(self, nums: list) -> int:
        if not nums:
            return -1
        count = [-1] * len(nums)
        for i in range(len(nums)):
            if count[nums[i]] == -1:
                count[nums[i]] = nums[i]
            else:
                return nums[i]
        return -1

    # 链式查找
    def findRepeatNumber(self, nums: list) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


nums = [4, 3, 1, 0, 2, 5, 3]
test = Solution()
print(test.findRepeatNumber(nums))
