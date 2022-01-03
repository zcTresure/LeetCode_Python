# -*- coding: utf-8 -*-
# File:      1185. 一周中的第几天.py
# DATA:      2022/1/3
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0
        days += 365 * (year - 1971) + (year - 1969) // 4
        days += sum(month_days[:month - 1])
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            days += 1
        days += day

        return week[(day + 3) % 7]


day, month, year = 31, 8, 2019
print(Solution().dayOfTheWeek(day, month, year))
