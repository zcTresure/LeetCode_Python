class Solution:
    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRows = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRows)
        return res


test = Solution()
ans = test.generate(5)
for i in range(len(ans)):
    print(ans[i])
