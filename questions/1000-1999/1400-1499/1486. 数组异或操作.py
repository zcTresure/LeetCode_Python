# File Name:  1486. 数组异或操作
# date:       2021/5/7
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= (start + i * 2)
        return ans


test = Solution()
n, start = 5, 0
print(test.xorOperation(n, start))
