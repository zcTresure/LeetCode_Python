# 枚举
class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        for i in range(n):
            for j in range(n):
                sub = s[i:j + 1]
                if sub and sub == sub[::-1]:
                    res += 1
        return res

    # 中心拓展
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        for i in range(2 * n - 1):
            left, right = i // 2, i // 2 + i % 2
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

    # 动态规划
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        dp = [[True] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                k = i + j
                if k >= n:
                    break
                if i == 0:
                    dp[i][k] = True
                elif i == 1:
                    dp[j][k] = (s[j] == s[k])
                else:
                    dp[j][k] = (dp[j + 1][k - 1] and s[j] == s[k])
                if dp[j][k]:
                    res += 1
        return res

    # Manacher/马拉车算法
    def countSubstrings(self, s: str) -> int:
        t = "-#"
        for c in s:
            t += c + '#'
        n = len(t)
        t += '-'
        Len = [0] * n
        iMax = rMax = ans = 0
        for i in range(n):
            Len[i] = min(rMax - i + 1, Len[2 * iMax - i]) if i <= rMax else 1
            while t[i + Len[i]] == t[i - Len[i]]:
                Len[i] += 1
            if (i + Len[i] - 1) > rMax:
                iMax = i
                rMax = i + Len[i] - 1
            ans += Len[i] // 2
        print(Len)
        return ans


s = "abc"
test = Solution()
print(test.countSubstrings(s))
