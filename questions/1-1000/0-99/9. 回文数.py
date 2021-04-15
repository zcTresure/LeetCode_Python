# File Name:  9. 回文数
# date:       2021/4/6
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)


x = int(input("输入数字："))
test = Solution()
print(test.isPalindrome(x))
