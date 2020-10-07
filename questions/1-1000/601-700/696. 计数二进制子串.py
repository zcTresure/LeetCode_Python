class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        tmp = 1
        cnt = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                tmp += 1
            else:
                cnt.append(tmp)
                tmp = 1
        cnt.append(tmp)
        print(cnt)
        for i in range(1, len(cnt)):
            res += min(cnt[i], cnt[i - 1])
        return res

    def countBinarySubstrings(self, s: str) -> int:
        res = pre = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, pre)
                pre = cur
                cur = 1
        res += min(cur, pre)
        return res


s = "10101"
s = "00110011"
test = Solution()
print(test.countBinarySubstrings(s))
