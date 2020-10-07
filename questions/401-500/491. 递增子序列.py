from collections import deque
from collections import defaultdict


class Solution:
    # 动态规划 + 哈希表
    def findSubsequences(self, nums: list) -> list:
        if not nums:
            return []
        dp = {(nums[0],)}
        for i in nums[1:]:
            dp.update({j + (i,)for j in dp if j[-1] <= i})
            dp.add((i,))
        return list([list(i)for i in dp if len(i) > 1])

    # 深搜 + 哈希表
    def findSubsequences(self, nums: list) -> list:
        res = []

        def dfs(nums: List[int], tmp: List[int]) -> None:
            if len(tmp) > 1:
                res.append(tmp)
            curPres = defaultdict(int)
            for index, i in enumerate(nums):
                if curPres[i]:
                    continue
                if not tmp or i >= tmp[-1]:
                    curPres[i] = 1
                    dfs(nums[index + 1:], tmp + [i])

        dfs(nums, [])
        return res

    # 广搜 + 哈希表
    def findSubsequences(self, nums: list) -> list:
        res = []
        d = deque([(nums, [])])
        while d:
            cur, new = d.popleft()
            if len(new) > 1:
                res.append(new)
            curPres = defaultdict(int)
            for inx, i in enumerate(cur):
                if curPres[i]:
                    continue
                if not new or i >= new[-1]:
                    curPres[i] = 1
                    d.append((cur[inx + 1:], new + [i]))
        return res


nums = [4, 6, 7, 7]
test = Solution()
print(test.findSubsequences(nums))
