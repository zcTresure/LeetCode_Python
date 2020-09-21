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

    # 排序
    def findRepeatNumber(self, nums: list) -> int:
        if not nums:
            return -1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    # 桶排序
    def findRepeatNumber(self, nums: list) -> int:
        if not nums:
            return -1
        count = [0] * len(nums)
        for i in range(len(nums)):
            if count[nums[i]] == 0:
                count[nums[i]] = nums[i]
            else:
                return nums[i]

    # 链表排序
    def findRepeatNumber(self, nums: list) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


nums = [2, 3, 1, 0, 2, 5, 3]
test = Solution()
print(test.findRepeatNumber(nums))
