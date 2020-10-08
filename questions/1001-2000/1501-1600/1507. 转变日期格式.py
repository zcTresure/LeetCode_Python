class Solution:
    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return str(date[-4:]) + '-' + ('0' if month.index(date[-8:-5]) + 1 < 10 else '') + str(
            month.index(date[-8:-5]) + 1) + '-' + (
                   date[0:2] if '0' <= date[1] <= '9' else '0' + date[0])


date = "20th Oct 2052"
test = Solution()
print(test.reformatDate(date))
