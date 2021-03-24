# Date:       2020/12/25
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, m, n = 0, 0, len(g), len(s)
        count = 0
        while i < m and j < n:
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count


g = [1, 2, 3]
s = [1, 2, 2, 3, 4]
test = Solution()
print(test.findContentChildren(g, s))
