class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        close = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sums = nums[left] + nums[right] + nums[i]
                if abs(sums - target) < abs(close - target):
                    close = sums
                if sums == target:
                    return target
                elif sums > target:
                    right -= 1
                else:
                    left += 1
        return close


nums = [-1, 2, 1, -4]
target = 1
test = Solution()
print(test.threeSumClosest(nums, target))
