# 动态规划
# 打家劫舍状态转移方程：dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
# 状态转移方程：dp[i] = max(dp[i - 2] + counter[i] * i, dp[i - 1])


from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        dic = dict(Counter(nums))
        alist = sorted(dic.keys())
        dp = [0] * (len(alist) + 1)
        dp[0] = 0
        pre = alist[0]
        dp[1] = alist[0] * dic.get(alist[0])
        for i in range(1, len(alist)):
            if alist[i] - pre > 1:
                dp[i + 1] = dp[i] + alist[i] * dic.get(alist[i])
            else:
                dp[i + 1] = max(dp[i], dp[i - 1] + alist[i]
                                * dic.get(alist[i]))
            pre = alist[i]
        return dp[-1]
# class Solution:
#     def deleteAndEarn(self, nums: list) -> int:
#         n = len(nums)
#         if n == 0:
#             return 0
#         maxnum = max(nums)
#         if n < 2:
#             return max(nums)
#         counter = [0] * (maxnum + 1)
#         for i in range(n):
#             counter[nums[i]] += 1
#         dp = [0] * (maxnum + 1)
#         dp[1] = counter[1] * 1
#         dp[2] = max(dp[1], dp[2] * 2)
#         for i in range(2, maxnum + 1):
#             dp[i] = max(dp[i - 2] + counter[i] * i, dp[i - 1])
#         return dp[-1]


nums = [2, 2, 3, 3, 3, 4]
print(Solution.deleteAndEarn(1, nums))
