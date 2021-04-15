# File Name:  191. 位1的个数
# date:       2021/3/22
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret


n = 1011
test = Solution()
print(bin(test.hammingWeight(n)))
