

__author__ = "zcTresure"


class Solution:
    def largestPerimeter(self, A: list) -> int:
        n = len(A)
        if n < 3:
            return 0
        A.sort()
        a, b, c = A[n - 3], A[n - 2], A[n - 1]
        for i in range(n - 4, -1, -1):
            print(a, b, c)
            if a + b > c:
                return a + b + c
            else:
                a, b, c = A[i], a, b
        if a + b > c:
            return a + b + c
        return 0

    def largestPerimeter(self, A: list) -> int:
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            if A[i - 2] + A[i - 1] > A[i]:
                return A[i - 2] + A[i - 1] + A[i]
        return 0


A = [2, 1, 2]
test = Solution()
print(test.largestPerimeter(A))
