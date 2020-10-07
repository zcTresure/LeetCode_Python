class Solution:
    def movesToMakeZigzag(self, nums: int) -> int:
        N = len(nums)
        res1, res2 = 0, 0
        for i in range(N):
            # 调整奇数位置大小
            if i % 2 == 0:
                d1 = nums[i] - nums[i - 1] + \
                    1 if i > 0 and nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - nums[i + 1] + 1 if i < N - \
                    1 and nums[i] >= nums[i + 1] else 0
                res1 += max(d1, d2)
        # 调整奇数位置大小
            else:
                d1 = nums[i] - nums[i - 1] + 1 if nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - nums[i + 1] + 1 if i < N - \
                    1 and nums[i] >= nums[i + 1] else 0
                res2 += max(d1, d2)
        return min(res1, res2)


nums = [1, 2, 3, 4, 5, 6]
test = Solution()
print(test.movesToMakeZigzag(nums))
