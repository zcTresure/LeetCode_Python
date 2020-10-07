import collections


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        num_times = collections.defaultdict(int)
        num_times[0] = 1
        n = len(nums)
        ans = cur_sum = 0
        for right in range(n):
            cur_sum += nums[right]
            if cur_sum - k in num_times:
                ans += num_times[cur_sum - k]
            num_times[cur_sum] += 1
        return ans


nums = [1, 1, 1]
k = 2
test = Solution()
print(test.subarraySum(nums, k))
