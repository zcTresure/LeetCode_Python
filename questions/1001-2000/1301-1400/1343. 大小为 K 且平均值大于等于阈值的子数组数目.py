# 首先遍历数组，将累计和存储到一个新的数组中（注意该数组的长度应该比原数组多1）
# 构建长度为k的滑动窗口，窗口的左右端口差值为中间k个数字的和
# 注意子数组顺序与原数组一致
class Solution:
    def numOfSubarrays(self, arr: list, k: int, threshold: int) -> int:
        res = [0]
        sub_sum, ans = k * threshold, 0
        for i in range(len(arr)):
            res.append(res[-1] + arr[i])
        for i in range(len(res) - k):
            b = res[i + k]
            a = res[i]
            if (b - a) >= sub_sum:
                ans += 1
        return ans


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k, threshold = 3, 4
test = Solution()
print(test.numOfSubarrays(arr, k, threshold))
