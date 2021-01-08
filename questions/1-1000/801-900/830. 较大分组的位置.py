# Date:       2021/1/5
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        s = s + '_'
        ans = []
        cnt = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if cnt > 2:
                    ans.append([i - cnt, i - 1])
                cnt = 1
            else:
                cnt += 1
        return ans


s = "abcdddeeeeaabbbcd"
test = Solution()
print(test.largeGroupPositions(s))
