# Date:       2020/12/23
# encode:      UTF-8
__author__ = "zcTresure"

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1


s = 'lolveetcode'
test = Solution()
print(test.firstUniqChar(s))
