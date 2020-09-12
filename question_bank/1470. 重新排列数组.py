class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res
