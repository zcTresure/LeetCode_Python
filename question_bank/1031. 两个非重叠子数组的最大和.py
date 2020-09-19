class Solution:
    def maxSumTwoNoOverlap(self, A: list, L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            # 分别包括了 L 个子数组在前和 M 个子数组在前
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res


A = [0, 6, 5, 2, 2, 5, 1, 9, 4]
L, M = 1, 2
print(Solution().maxSumTwoNoOverlap(A, L, M))
