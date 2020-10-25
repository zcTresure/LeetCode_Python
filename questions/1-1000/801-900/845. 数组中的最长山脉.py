class Solution:
    # 枚举
    def longestMountain(self, A: list) -> int:
        n = len(A)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            left[i] = (left[i - 1] + 1 if A[i - 1] < A[i] else 0)
        for i in range(n - 2, -1, -1):
            right[i] = (right[i + 1] + 1 if A[i + 1] < A[i] else 0)
        res = 0
        for i in range(n):
            if left[i] and right[i]:
                res = max(res, (left[i] + right[i]) + 1 if left[i] + right[i] else 0)
        return res

    #


A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test = Solution()
print(test.longestMountain(A))


def longestMountain(self, A: list) -> int:
    n = len(A)
    res = left = 0
    while left + 2 < n:
        right = left + 1
        if A[left] < A[left + 1]:
            while right + 1 < n and A[right] < A[right + 1]:
                right += 1
            if right < n - 1 and A[right] > A[right + 1]:
                while right + 1 < n and A[right] > A[right + 1]:
                    right += 1
                res = max(res, right - left + 1)
            else:
                right += 1
        left = right
    return res