class Solution:
    # 回溯
    def combinationSum3(self, k: int, n: int) -> list:
        ans = list()

        def backtrack(tmp: list, index: int, k: int, n: int):
            if len(tmp) == k and n == sum(tmp):
                ans.append(tmp[:])
                return
            for i in range(index, min(n, 10)):
                tmp.append(i)
                backtrack(tmp, i + 1, k, n)
                tmp.pop()
        backtrack([], 1, k, n)
        return ans


n, k = 9, 3
test = Solution()
print(test.combinationSum3(k, n))
