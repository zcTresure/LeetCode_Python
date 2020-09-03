# 双指针
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         m, n = len(s), len(t)
#         i = j = 0
#         while i < m and j < n:
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == m
# 动态规划？ 看不懂
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]
        print(f)
        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1
        
        return True



s = "abc"
t = "ahbgdc"
print(Solution.isSubsequence(1, s, t))
