import itertools


class Solution:
    def combine(self, n: int, k: int) -> list:
        ans = list()

        def backtrack(tmp: list, index: int) -> None:
            if len(tmp) == k:
                ans.append(tmp[:])
                return
            for i in range(index, n + 1):
                tmp.append(i)
                backtrack(tmp, i + 1)
                tmp.pop()
        backtrack(list(), 1)
        return ans

    # 迭代器
    def combine(self, n: int, k: int) -> list:
        return list(itertools.combinations(range(1, n + 1), k))


n = 9
k = 2
test = Solution()
print(test.combine(n, k))
