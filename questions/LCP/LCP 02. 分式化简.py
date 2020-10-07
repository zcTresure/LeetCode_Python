class Solution:
    def fraction(self, cont: list) -> list:
        a, b = -1, -1
        n = len(cont) - 1
        for i in range(n, -1, -1):
            if i == n:
                a, b = cont[-1], 1
            else:
                a, b = cont[i] * a + b, a
        return [a, b]


cont = [3, 2, 0, 2]
test = Solution()
print(test.fraction(cont))
