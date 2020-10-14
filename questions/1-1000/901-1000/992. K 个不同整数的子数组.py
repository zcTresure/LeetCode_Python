from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, A: list, K: int) -> int:
        def get(A: int, K: int) -> int:
            count = Counter()
            res, left = 0, 0
            for i in range(len(A)):
                if count[A[i]] == 0:
                    K -= 1
                count[A[i]] += 1
                while K < 0:
                    count[A[left]] -= 1
                    if count[A[left]] == 0:
                        K += 1
                    left += 1
                res += i - left + 1
            return res

        return get(A, K) - get(A, K - 1)


A = [1, 2, 1, 2, 3]
K = 2
test = Solution()
print(test.subarraysWithKDistinct(A, K))
