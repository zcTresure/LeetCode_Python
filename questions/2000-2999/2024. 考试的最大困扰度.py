# -*- coding: utf-8 -*-
# File:      2024. 考试的最大困扰度.py
# DATA:      2022/3/29
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(ch: str) -> int:
            ans, left, sum = 0, 0, 0
            for right in range(len(answerKey)):
                sum += answerKey[right] != ch
                while sum > k:
                    sum -= answerKey[left] != ch
                    left += 1
                ans = max(ans, right - left + 1)
            return ans

        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))


print(Solution().maxConsecutiveAnswers(answerKey="TTFF", k=2))
print(Solution().maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1))
