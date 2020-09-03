class Solution:
    def sumSubarrayMins(self, A: list) -> int:
        n = len(A)
        ans = sum(A)
        j = 2
        while j <= n:
            for i in range(n):
                print(ans, i, A[i:i + j])
                if i + j <= n:
                    ans += min(A[i:i + j])
                i += j
            j += 1
        return ans


print(Solution.sumSubarrayMins(1, A))
