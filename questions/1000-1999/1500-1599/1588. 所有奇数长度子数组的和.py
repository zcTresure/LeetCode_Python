class Solution:
    def sumOddLengthSubarrays(self, arr: list) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            leftOdd, leftEven = (i + 1) // 2, i // 2 + 1
            rightOdd, rightEven = (n - i) // 2, (n - i - 1) // 2 + 1
            ans += arr[i] * (leftOdd * rightOdd + leftEven * rightEven)
        return ans


arr = [1, 4, 2, 5, 3]
test = Solution()
print(test.sumOddLengthSubarrays(arr))
