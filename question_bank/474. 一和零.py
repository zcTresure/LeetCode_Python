class Solution:
    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        if len(strs) == 0:
            return 0
        else:
            res = [[0] * (n + 1) for _ in range(m + 1)]
            for string in strs:
                ones = string.count("1")
                zeroes = string.count("0")
                for i in range(m, zeroes - 1, -1):
                    for j in range(n, ones - 1, -1):
                        res[i][j] = max(
                            res[i][j], res[i - zeroes][j - ones] + 1)
                    for i in range(n + 1):
                        print(res[i])
            return res[m][n]


Array = {"10", "0001", "111001", "1", "0"}
m, n = 5, 3
print(Solution.findMaxForm(1, Array, m, n))
