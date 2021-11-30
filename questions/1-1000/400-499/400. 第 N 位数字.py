# -*- coding: utf-8 -*-
# File:      400. 第 N 位数字.py
# DATA:      2021/11/30
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 二分查找
    def totalDigit(self, length: int) -> int:
        digit, cur_cnt = 0, 9
        for cnt_len in range(1, length + 1):
            digit += cur_cnt * cnt_len
            cur_cnt *= 10
        return digit

    def findNthDigit(self, n: int) -> int:
        low, high = 1, 9
        while low < high:
            mid = (low + high) // 2
            if self.totalDigit(mid) < n:
                low = mid + 1
            else:
                high = mid
        d = low
        pre_digit = self.totalDigit(d - 1)
        index = n - pre_digit - 1
        start = 10 ** (d - 1)
        num = start + index // d
        digit_idx = index % d
        return num // 10 ** (d - digit_idx - 1) % 10

    # 直接计算
    def findNthDigit(self, n: int) -> int:
        base, digit_cnt = 1, 1
        while n > base * 9 * digit_cnt:
            n -= base * 9 * digit_cnt
            base *= 10
            digit_cnt += 1
        n -= 1
        return int(str(base + n // digit_cnt)[n % digit_cnt])


if __name__ == '__main__':
    n = int(input())
    print(Solution().findNthDigit(n))
