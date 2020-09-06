import re


class Solution:
    # 贪心
    def minCost(self, s: str, cost: list) -> int:
        n = len(s)
        if n < 2:
            return 0
        ans = index = 0
        for i in range(1, n):
            if s[i] == s[index]:
                j = i if cost[i] < cost[index] else index
                ans += cost[j]
                if j == index:
                    index = i
            else:
                index = i
        return ans

    # 正则 找出连续相同中最大的那个字符
    def minCost(self, s: str, cost: list) -> int:
        res = 0
        for m in re.finditer(r'(\w)\1+', s):
            index = slice(*m.span())
            res += sum(cost[index]) - max(cost[index])
        return res


s = "aaabbbabbbb"
cost = [3, 5, 9, 7, 5, 3, 5, 5, 4, 8, 1]
test = Solution()
print(test.minCost(s, cost))
