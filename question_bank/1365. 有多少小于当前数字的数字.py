
class Solution:
    # 暴力
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        res = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            res.append(count)
        return res

    # 频次数组 + 前缀和
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        n = len(nums)
        cnt, res = [0] * 101, [0] * n
        for num in nums:
            cnt[num] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]
        for i in range(n):
            if nums[i]:
                res[i] = cnt[nums[i] - 1]
        return res

    # 排序
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        n = len(nums)
        res = [0] * n
        tmp = sorted([(nums[i], i) for i in range(n)])
        pre = -1
        for i in range(n):
            if i != 0 and tmp[i][0] != tmp[i - 1][0]:
                pre = i - 1
            res[tmp[i][1]] = pre + 1
        return res

    # 排序
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        res = list()
        num = sorted(nums)
        for i in nums:
            res.append(num.index(i))
        return res

    def smallerNumbersThanCurrent(self, nums: list) -> list:
        return [len(list(filter(lambda x: x < i, nums))) for i in nums]


solution = Solution()
nums = [8, 1, 2, 2, 3]
print(solution.smallerNumbersThanCurrent(nums))
