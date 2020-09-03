class Solution:
    def replaceElements(self, arr: list) -> list:
        n = len(arr)
        res = [-1] * n
        for i in range(n - 2, -1, -1):
            res[i] = max(res[i + 1], arr[i + 1])
        return res


arr = [17, 18, 5, 4, 6, 1]
test = Solution()
print(test.replaceElements(arr))
