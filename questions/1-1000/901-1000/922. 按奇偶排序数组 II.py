# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"


class Solution:
    def sortArrayByParityII(self, A: list) -> list:
        n = len(A)
        ans = [0] * n
        i = 0
        for a in A:
            if a % 2 == 0:
                ans[i] = a
                i += 2
        i = 1
        for a in A:
            if a % 2 == 1:
                ans[i] = a
                i += 2
        return ans

    def sortArrayByParityII(self, A: list) -> list:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 == 1:
                while A[j] % 2 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


A = [4, 2, 5, 7]
test = Solution()
print(test.sortArrayByParityII(A))
