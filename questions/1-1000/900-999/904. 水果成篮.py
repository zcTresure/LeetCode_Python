from itertools import groupby
from collections import Counter


class Solution:
    # 块处理
    def totalFruit(self, tree: list) -> int:
        blocks = [(k, len(list(v))) for k, v in groupby(tree)]
        ans = i = 0
        while i < len(blocks):
            types, weight = set(), 0
            for j in range(i, len(blocks)):
                types.add(blocks[j][0])
                weight += blocks[j][1]
                if len(types) >= 3:
                    i = j - 1
                    break
                ans = max(ans, weight)
        return ans

    # 滑动窗口
    def totalFruit(self, tree: list) -> int:
        ans = i = 0
        count = Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans


tree = [3, 3, 3]
test = Solution()
print(test.totalFruit(tree))
