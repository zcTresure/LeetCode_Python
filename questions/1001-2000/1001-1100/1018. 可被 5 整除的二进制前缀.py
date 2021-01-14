# Date:       2021/1/14
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def prefixesDivBy5(self, A: list) -> list:
        res = list()
        num = 0
        for bit in A:
            num = (num * 2 + bit) % 5
            res.append(num == 0)
        return res


A = [0, 1, 1, 1, 1, 1]
print(Solution().prefixesDivBy5(A))
