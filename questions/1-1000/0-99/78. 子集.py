import itertools


class Solution:
    # 回溯
    def subsets(self, nums: list) -> list:
        def trackback(cur: list, index: int) -> None:
            cur.append(nums[index])
            res.append(cur[:])
            for i in range(index + 1, len(nums)):
                trackback(cur, i)
                cur.pop()

        res = list()
        res.append([])
        for i in range(len(nums)):
            trackback([], i)
        return res

    # 库函数
    def subsets(self, nums: list) -> list:
        res = list()
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(list(tmp))
        return res

    # 迭代
    def subsets(self, nums: list) -> list:
        res = [[]]
        for num in nums:
            res += [[num] + i for i in res]
        return res


nums = [1, 2, 3]
test = Solution()
res = test.subsets(nums)
sorted(res)
for row in res:
    print(row)
