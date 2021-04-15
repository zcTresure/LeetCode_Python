class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res


nums = [2, 5, 1, 3, 4, 7]
n = 3
test = Solution()
print(test.shuffle(nums, n))
