from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        lenp = len(p)
        p = "".join(sorted(p))
        res = []
        for i in range(len(s) - len(p) + 1):
            if "".join(sorted(s[i:i + lenp])) == p:
                res.append(i)
        return res

    def findAnagrams(self, s: str, p: str) -> list:
        lens, lenp = len(s), len(p)
        res = list()
        p = Counter(p)
        prefix = [0] * (lens + 1)
        prefix[0] = Counter()
        for i in range(1, lens + 1):
            prefix[i] = prefix[i - 1].copy()
            prefix[i][s[i - 1]] += 1
            if i >= lenp and prefix[i] - prefix[i - lenp] == p:
                res.append(i - lenp)
        return res

    def findAnagrams(self, s: str, p: str) -> list:
        countP = [0] * 26
        countS = [0] * 26
        res = []
        for c in p:
            countP[ord(c) - 97] += 1
        left = 0
        for right in range(len(s)):
            if right < len(p) - 1:
                countS[ord(s[right]) - 97] += 1
                continue
            countS[ord(s[right]) - 97] += 1
            if countP == countS:
                res.append(left)
            countS[ord(s[left]) - 97] -= 1
            left += 1
        return res


s = "cbaebabacd"
p = "abc"
test = Solution()
print(test.findAnagrams(s, p))
