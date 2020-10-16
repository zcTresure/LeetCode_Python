class Solution:
    def sortedSquares(self, A: list) -> list:
        for i in range(len(A)):
            A[i] = -A[i] if A[i] < 0 else A[i]
        A.sort()
        for i in range(len(A)):
            A[i] = A[i] ** 2
        return A

    def sortedSquares(self, A: list) -> list:
        return sorted(num * num for num in A)

    def sortedSquares(self, A: list) -> list:
        n = len(A)
        negative = -1
        for i, num in enumerate(A):
            if num < 0:
                negative = i
            else:
                break
        ans = list()
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(A[j] * A[j])
                j += 1
            elif j == n:
                ans.append(A[i] * A[i])
                i -= 1
            elif A[i] * A[i] < A[j] * A[j]:
                ans.append(A[i] * A[i])
                i -= 1
            else:
                ans.append(A[j] * A[j])
                j += 1
        return ans

    def sortedSquares(self, A: list) -> list:
        n = len(A)
        ans = [0] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if A[i] * A[i] < A[j] * A[j]:
                ans[pos] = A[j] * A[j]
                j -= 1
            else:
                ans[pos] = A[i] * A[i]
                i += 1
            pos -= 1
        return ans


A = [-7, -3, 2, 3, 11]
test = Solution()
print(test.sortedSquares(A))
