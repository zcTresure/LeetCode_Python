class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        result = []
        candidates.sort()

        def backtrack(candidates, tmp):
            if sum(tmp) > target:
                return
            if sum(tmp) == target:
                result.append(tmp)
                return
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(candidates[i + 1:], tmp + [candidates[i]])
            return result
        return backtrack(candidates, [])


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
test = Solution()
print(test.combinationSum2(candidates, target))
