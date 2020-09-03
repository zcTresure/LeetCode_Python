class Solution:
    def findLongestSubarray(self, array: list) -> list:
        if not array:          # 数组为空直接输出
            return []

        def judge(c) -> bool:  # 判断元素为字符还是数字
            if 'A' <= c <= "Z" or 'a' <= c <= 'z':
                return True
            else:
                return False
        n = len(array)
        dp = [0] * n           # dp数组 用来记录前缀中字符-数字的个数
        dp[0] = 1 if judge(array[0]) else -1
        # 为字符时dp[i] = dp[i - 1] + 1 为数字时dp[i] = dp[i - 1] - 1
        for i in range(1, n):
            dp[i] = dp[i - 1] + 1 if judge(array[i]) else dp[i - 1] - 1
        dic = {}
        dic[0] = -1
        for i in range(n):
            dic[dp[i]] = dic.get(dp[i], i)
        max_len = left = right = 0
        for i in range(n):
            if (i - dic[dp[i]]) > max_len:
                left = dic[dp[i]]
                right = i + 1
                max_len = right - left
        return array[left + 1:right]


array = ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5",
         "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]
test = Solution()
print(test.findLongestSubarray(array))
