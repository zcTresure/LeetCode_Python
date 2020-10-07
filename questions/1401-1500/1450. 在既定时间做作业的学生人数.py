class Solution:
    def busyStudent(self, startTime: list, endTime: list, queryTime: int) -> int:
        ans = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ans += 1
        return ans


startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4
test = Solution()
print(test.busyStudent(startTime, endTime, queryTime))
