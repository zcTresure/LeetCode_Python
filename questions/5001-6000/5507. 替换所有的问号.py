import collections


class Solution:
    def modifyString(self, s: str) -> str:
        words = 'abcdefghijklmnopqrstuvwxyz'
        s += '0'
        ans = '0'
        for i in range(len(s)):
            if s[i] == '?':
                for j in range(len(words)):
                    if ans[i] == words[j] or s[i + 1] == words[j]: continue
                    else:
                        ans += words[j]
                        break
            else: ans += s[i]
        return ans[1:-1]


s = "?zs"
test = Solution()
print(test.modifyString(s))
