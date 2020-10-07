class Solution:
    def freqAlphabets(self, s: str) -> str:
        def get(st):
            return chr(int(st) + 96)
        i, ans = 0, ""
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                ans += get(s[i: i + 2])
                i += 2
            else:
                ans += get(s[i])
            i += 1
        return ans

    # 逆序
    def freqAlphabets(self, s: str) -> str:
        ans, i = '', len(s) - 1
        while i >= 0:
            if s[i] == '#':
                ans += chr(int(s[i - 2: i]) + 96)
                i -= 3
            else:
                ans += chr(int(s[i]) + 96)
                i -= 1
        return ans[:: -1]


s = "10#11#12"
print(Solution().freqAlphabets(s))
