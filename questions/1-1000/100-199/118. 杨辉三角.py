class Solution:
    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            new_rows = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(new_rows)
        return res


test = Solution()
print(Solution().generate(numRows=5))
