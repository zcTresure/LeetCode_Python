# 官解 动态规划
'''
def splitArray(self, nums: list, m: int) -> int:
    n = len(nums)
    dp = [[10**18] * (m + 1) for _ in range(n + 1)]
    sub_nums = [0]
    for i in range(n):
        sub_nums.append(sub_nums[-1] + nums[i])
    dp[0][0] = 0
    for i in range(n + 1):
        for j in range(1, min(i, m) + 1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], max(
                    dp[k][j - 1], sub_nums[i] - sub_nums[k]))

    return dp[n][m]
'''


def splitArray(self, nums: list, m: int) -> int:
    def check(x: int) -> bool:
        total, cnt = 0, 1
        for num in nums:
            if total + num > x:
                cnt += 1
                total = num
            else:
                total += num
        return cnt <= m
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

nums = [7, 2, 5, 10, 8]
m = 2
print(splitArray(1, nums, m))
