# File Name:  1043. 分隔数组以得到最大和
# date:       2021/3/24
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


# dp[i]代表子数组A:i按要求操作能得到的最大和，状态转移方程为：dp[i]=max(dp[j]+max(A[j:i])*(i-j))(i-K <= j < i)
# 其中j表示最后一个分割数组的起始下标，max(A[j:i])表示子数组A[j:i]的最大值，i-K <= j < i保证分割的数组长度不大于K
class Solution:
    # 动态规划
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            j = i - 1  # 每次从当前位置的前一位逆序查找最大值
            max_num = -float('inf')
            while i - j <= k and j >= 0:  # 向前运动但至少要有 k 位和下标不能越界
                max_num = max(max_num, arr[j])  # 更新最大值
                dp[i] = max(dp[i], dp[j] + max_num * (i - j))  # 状态转移方程
                j -= 1
        return dp[n]


test = Solution()
arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
print(test.maxSumAfterPartitioning(arr, k))
