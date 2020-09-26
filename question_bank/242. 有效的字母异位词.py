from collections import defaultdict
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = defaultdict(chr)
        dic_t = defaultdict(chr)
        for i in range(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = 1
            else:
                dic_s[s[i]] += 1
            if t[i] not in dic_t:
                dic_t[t[i]] = 1
            else:
                dic_t[t[i]] += 1
        print(dic_s)
        print(dic_t)
        if dic_s == dic_t:
            return True
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s = "aaccca"
t = "caccaa"
test = Solution()
print(test.isAnagram(s, t))
