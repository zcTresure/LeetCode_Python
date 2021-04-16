# File Name:  87. 扰乱字符串
# date:       2021/4/16
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import Counter
from linecache import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache  # 第一个字符串从 i1 开始，第二个字符串从 i2 开始，子串的长度为 length，是否和谐
        def dfs(i1, i2, length):
            if s1[i1:i1 + length] == s2[i2:i2 + length]:  # 判断两个子串是否相等
                return True
            if Counter(s1[i1:i1 + length]) != Counter(s2[i2:i2 + length]):  # 判断是否存在字符 c 在两个子串中出现的次数不同
                return False
            for i in range(1, length):  # 枚举分割位置
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):  # 不交换的情况
                    return True
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):  # 交换的情况
                    return True
            return False

        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans


s1 = "great"
s2 = "rgeat"
test = Solution()
print(test.isScramble(s1, s2))
