# Date:       2021/1/22
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        B = []
        while K:
            B.append(K % 10)
            K //= 10
        B.reverse()
        x = 0
        m, n = len(A), len(B)
        ans = []
        while m and n:
            x = x + A[m - 1] + B[n - 1]
            ans.append(x % 10)
            x //= 10
            m -= 1
            n -= 1
        while m:
            x = x + A[m - 1]
            ans.append(x % 10)
            x //= 10
            m -= 1
        while n:
            x = x + B[n - 1]
            ans.append(x % 10)
            x //= 10
            n -= 1
        if x:
            ans.append(x)
        ans.reverse()
        return ans

    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = []
        n = len(A)
        for i in range(n - 1, -1, -1):
            sum = A[i] + K % 10
            K //= 10
            if sum >= 10:
                K += 1
                sum %= 10
            ans.append(sum)
        while K:
            ans.append(K % 10)
            K //= 10
        ans.reverse()
        return ans


A = [2, 7, 4]
K = 181
test = Solution()
print(test.addToArrayForm(A, K))
