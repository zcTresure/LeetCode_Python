# Date:       2020/12/10
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def lemonadeChange(self, bills: list) -> bool:
        count5, count10 = 0, 0
        for dollars in bills:
            if dollars == 5:
                count5 += 1
            elif dollars == 10:
                count5 -= 1
                count10 += 1
            elif dollars == 20:
                if count10 > 0:
                    count10 -= 1
                else:
                    count5 -= 2
                count5 -= 1
            if count5 < 0 or count10 < 0:
                return False
        return True


bills = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]
test = Solution()
print(test.lemonadeChange(bills))
