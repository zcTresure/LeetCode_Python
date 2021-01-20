class Solution:
    # 排序 将两个绝对值最大的负数 和 第二大和第三大的数字相比较
    def maximumProduct(self, nums: list) -> int:
        nums.sort()
        return nums[len(nums) - 1] * max(nums[0] * nums[1], nums[len(nums) - 3],
                                         nums[len(nums) - 2] * nums[len(nums) - 3])

    # 线性扫描
    def maximumProduct(self, nums: list) -> int:
        min1 = min2 = min3 = float('inf')
        max1 = max2 = max3 = -float('inf')
        for num in nums:
            if num <= min1:
                min1, min2, min3 = num, min1, min2
            elif num <= min2:
                min2, min3 = num, min2
            elif num <= min3:
                min3 = num
            if num >= max1:
                max1, max2, max3 = num, max1, max2
            elif num >= max2:
                max2, max3 = num, max2
            elif num >= max3:
                max3 = num
        return max(max1 * max2 * max3, max1 * min1 * min2, min1 * min2 * min3)


nums = [[1, 2, 3, 4],
        [-1, -2, 0, 1],
        [-1, -2, -3, -4]]

test = Solution()
for i in range(len(nums)):
    print(test.maximumProduct(nums[i]))
