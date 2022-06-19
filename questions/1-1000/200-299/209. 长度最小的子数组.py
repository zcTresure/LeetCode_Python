from bisect import bisect_left
from typing import List


class Solution:
    # 暴力 会超出时间限制
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        ans = float("inf")
        for i in range(n):
            for j in range(i, n):
                sums = 0
                for k in range(i, j + 1):
                    sums += nums[k]
                    if sums >= s:
                        ans = min(ans, (k - i + 1))
                        break
        return ans if ans != float('inf') else 0

    # 优化的暴力 也会超出时间限制
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float("inf")
        sums = [0] * n
        sums[0] = nums[0]
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]
        for i in range(n):
            for j in range(i, n):
                sum = sums[j] - sums[i] + nums[i]
                if sum >= s:
                    ans = min(ans, (j - i + 1))
                    break
        return ans if ans != float('inf') else 0

    # 前缀和 + 二分查找
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect_left(sums, target)
            if bound != n + 1:
                ans = min(ans, bound - (i - 1))
        return 0 if ans == n + 1 else ans

    # 双指针
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float("inf")
        sum = left = 0
        for right in range(n):
            sum += nums[right]
            while sum >= s:
                ans = min(ans, (right - left + 1))
                sum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0


print(Solution().minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))
