# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"


class Solution:
    def validMountainArray(self, A: list) -> bool:
        n = len(A)
        i = 0
        while i + 1 < n and A[i] < A[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and A[i] > A[i + 1]:
            i += 1
        return i == n - 1


A = [0, 3, 2, 1]
test = Solution()
print(test.validMountainArray(A))
