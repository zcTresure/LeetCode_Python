# File Name:  7. 整数反转
# date:       2021/4/6
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            y = x[::-1]
            if int(y) not in range(-2 ** 31, 2 ** 31):
                return 0
            return int(y)
        else:
            x = str(abs(x))
            y = x[::-1]
            z = '-' + y
            if int(z) not in range(-2 ** 31, 2 ** 31):
                return 0
            return int(z)


x = int(input("输入数字："))
test = Solution()
print(test.reverse(x))
