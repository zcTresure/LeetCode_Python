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

    def sumSubarrayMins(self, A: list) -> int:
        n = len(A)
        stack = []
        prev = [None] * n
        for i in range(n):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        stack.clear()
        nxt = [None] * n
        for k in range(n - 1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            nxt[k] = stack[-1] if stack else n
            stack.append(k)

        return sum((i - prev[i]) * (nxt[i] - i) * A[i]
                   for i in range(n)) % (10**9 + 7)


A = [3, 1, 2, 4]
test = Solution()
print(test.sumSubarrayMins(A))
