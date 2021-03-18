# File Name:  3. 无重复字符的最长子串
# date:       2021/3/18
# oding:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()  # 哈希集合，记录每个字符是否出现过
        tmp, ans = 0, 0  # 当前无重复字串长度 和 无重复最长字串长度
        for i in range(len(s)):
            while s[i] in char:  # 将重复出现的字符和之前的字符全部清除，重新计数
                char.remove(s[i - tmp])
                tmp -= 1
            char.add(s[i])  # 重复字符已经在集合中删除，再将当前字符加入集合
            tmp += 1
            ans = max(tmp, ans)
        return ans


s = "pwwkew"
test = Solution()
print(test.lengthOfLongestSubstring(s))
