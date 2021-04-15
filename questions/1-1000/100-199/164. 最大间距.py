

__author__ = "zcTresure"


class Solution:
    class Solution:
        class Solution:
            def maximumGap(self, nums: list) -> int:
                if len(nums) < 2:
                    return 0
                maxL = -1
                nums.sort()
                for i in range(1, len(nums)):
                    maxL = max(maxL, nums[i] - nums[i - 1])
                return maxL

        def maximumGap(self, nums: list) -> int:
            n = len(nums)
            if n < 2:
                return 0
            buf = [0] * n
            exp = 1
            maxVal = max(nums)
            while maxVal >= exp:
                cnt = [0] * 10
                for i in range(n):
                    digit = (nums[i] // exp) % 10
                    cnt[digit] += 1
                for i in range(1, 10):
                    cnt[i] += cnt[i - 1]
                for i in range(n - 1, -1, -1):
                    digit = (nums[i] // exp) % 10
                    buf[cnt[digit] - 1] = nums[i]
                    cnt[digit] -= 1
                nums = buf[:]
                exp *= 10
            res = 0
            for i in range(n):
                res = max(res, nums[i] - nums[i - 1])
            return res

    def maximumGap(self, nums: list) -> int:
        n = len(nums)
        if n < 2:
            return 0
        maxVal, minVal, maxGap = max(nums), min(nums), 0
        eachBucketLen = max(1, (maxVal - minVal) // (len(nums) - 1))  # 桶的长度
        buckets = [[] for _ in range((maxVal - minVal) // eachBucketLen + 1)]  # 桶的数量
        for i in range(len(nums)):
            loc = (nums[i] - minVal) // eachBucketLen
            buckets[loc].append(nums[i])
        prevMax = float('inf')
        for i in range(len(buckets)):
            if buckets[i] and prevMax != float('inf'):
                maxGap = max(maxGap, min(buckets[i]) - prevMax)
            if buckets[i]:
                prevMax = max(buckets[i])
        return maxGap


nums = [3, 6, 9, 1]
test = Solution()
print(test.maximumGap(nums))
