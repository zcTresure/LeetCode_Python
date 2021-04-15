class Solution:
    def kConcatenationMaxSum(self, arr: list, k: int) -> int:
        if not arr:
            return 0
        maxSum, tmp = 0, 0
        length = len(arr)
        # 计算两个数组串联后的最大值
        for i in range(length * min(2, k)):
            tmp = max(tmp + arr[i % length], arr[i % length])
            maxSum = max(maxSum, tmp)
        # 一个数组和为正时，需要加上k-2个数组和 ps还可以快速幂继续优化
        if k <= 2:
            return maxSum
        return (maxSum + max(sum(arr), 0) * (k - 2)) % 1000000007


arr = [-5, 4, -4, -3, 5, -3]
k = 3
test = Solution()
print(test.kConcatenationMaxSum(arr, k))
