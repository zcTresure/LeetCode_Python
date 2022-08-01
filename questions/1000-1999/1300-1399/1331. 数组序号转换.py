from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [ranks[i] for i in arr]


arr = [10, 10, 20, 30]
test = Solution()
print(test.arrayRankTransform(arr))
