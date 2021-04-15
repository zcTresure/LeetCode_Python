class Solution:
    def countBits(self, num: int) -> list:
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 1:
                res[i] = res[i - 1] + 1
            else:
                res[i] = res[i // 2]
        return res

    def countBits(self, num: int) -> list:
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i & (i - 1)] + 1
        return res


test = Solution()
print(test.countBits(5))
