class Solution:
    def smallestDistancePair(self, nums: list, k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            cnt, start = 0, 0
            for i in range(len(nums)):
                while nums[i] - nums[start] > mid:
                    start += 1
                cnt += i - start
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left


nums = [1, 3, 1]
k = 1
test = Solution()
print(test.smallestDistancePair(nums, k))
