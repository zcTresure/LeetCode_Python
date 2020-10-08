class Solution:
    def dayOfYear(self, date: str) -> int:
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year = True if int(date[0:4]) % 400 == 0 or (int(date[:4]) % 4 == 0 and int(date[:4]) % 100 != 0) else False
        m = sum(month[:int(date[5:7]) - 1]) + (1 if year and date[5:7] > '02' else 0)
        return m + int(date[8:])


date = "2016-03-01"
test = Solution()
print(test.dayOfYear(date))
