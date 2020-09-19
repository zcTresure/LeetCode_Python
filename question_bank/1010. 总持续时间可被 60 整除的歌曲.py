class Solution:
    def numPairsDivisibleBy60(self, time: list) -> int:
        n = len(time)
        dic = [0] * 60
        ans = 0
        for i in range(n):
            temp = time[i] % 60
            dic[temp] += 1
        for i in range(1, 30):
            if dic[i] != 0 and dic[60 - i] != 0:
                ans += dic[i] * dic[60 - i]
        ans += dic[0] * (dic[0] - 1) // 2 + dic[30] * (dic[30] - 1) // 2
        return ans


time = [60, 60, 60]
print(Solution().numPairsDivisibleBy60(time))
