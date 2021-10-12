# -*- coding: utf-8 -*-
# File:      273. 整数转换英文表示.py
# DATA:      2021/10/11
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def numberToWords(self, num: int) -> str:
        singles = ['', 'One', 'Two', 'Three', 'Four', "Five", 'Six', 'Seven', 'Eight', 'Nine']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                 'Nineteen']
        tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']

        if num == 0:
            return "Zero"

        def toEnglish(num: int) -> str:
            s = ""
            if num >= 100:
                s += singles[num // 100] + " Hundred "
                num %= 100
            if num >= 20:
                s += tens[num // 10] + " "
                num %= 10
            if 0 < num < 10:
                s += singles[num] + " "
            elif num >= 10:
                s += teens[num - 10] + " "
            return s

        ans = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                ans += toEnglish(curNum) + thousands[i] + " "
            unit //= 1000
        return ans.strip()


num = 50868
print(Solution().numberToWords(num))
