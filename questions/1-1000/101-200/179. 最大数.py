# File Name:  179. 最大数
# date:       2021/9/12
# encode:      UTF-8
__author__ = 'zcTresure'


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: list) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


nums = [10, 2]
test = Solution()
print(test.largestNumber(nums))
