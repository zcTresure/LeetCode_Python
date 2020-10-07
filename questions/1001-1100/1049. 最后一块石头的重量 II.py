class Solution:
    def lastStoneWeightII(self, stones: list) -> int:
        target = sum(stones) / 2
        n = len(stones)
        candidates = {0}
        for x in stones:
            addition = set()
            for y in candidates:
                if x + y == target:
                    return 0
                if x + y < target:
                    addition.add(x + y)
            candidates = candidates.union(addition)
        return int(2 * (target - max(candidates)))


stones = [2, 7, 4, 1, 8, 1]
print(Solution.lastStoneWeightII(1, stones))
