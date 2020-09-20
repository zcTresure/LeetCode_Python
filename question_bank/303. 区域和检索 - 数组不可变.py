import collections


class NumArray:
    # 暴力
    def __init__(self, nums: list):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        sums = 0
        for index in range(i, j + 1):
            sums += self.nums[index]
        return sums

    # 字典缓存
    def __init__(self, nums: list):
        self.dic = collections.defaultdict()
        for i in range(len(nums)):
            sums = 0
            for j in range(i, len(nums)):
                sums += nums[j]
                self.dic[(i, j)] = sums

    def sumRange(self, i: int, j: int) -> int:
        return self.dic[(i, j)]

    # 动态规划 数组缓存
    def __init__(self, nums: list):
        self.dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.dp[i + 1] = self.dp[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j + 1] - self.dp[i]


nums = [-2, 0, 3, -5, 2, -1]
test = NumArray(nums)
print(test.sumRange(0, 3))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
