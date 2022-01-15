# -*- coding: utf-8 -*-
# File:    1716. 计算力扣银行的钱.py
# Date:    2022/1/15
# Software: Pycharm
__author__ = 'zcFang'


class Solution:
    def totalMoney(self, n: int) -> int:
        week, day = 1, 1
        ans = 0
        for i in range(n):
            ans += week + day - 1
            day += 1
            if day == 8:
                day = 1
                week += 1
        return ans

    def totalMoney(self, n: int) -> int:
        # 所有完整的周存的钱
        weeks = n // 7
        firstWeek = (1 + 7) * 7 // 2
        lastWeek = firstWeek + 7 * (weeks - 1)
        weekMoney = (firstWeek + lastWeek) * weeks // 2
        # 剩下的不能构成一个完整的周的天数里存的钱
        days = n % 7
        firstDayMoney = 1 + weeks
        lastDayMoney = firstDayMoney + days - 1
        dayMoney = (firstDayMoney + lastDayMoney) * days // 2
        return weekMoney + dayMoney


print(Solution().totalMoney(n=10))
