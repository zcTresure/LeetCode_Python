class Solution:
    def reverseString(self, s: list) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


s = ["h", "e", "l", "l", "o"]
test = Solution()
test.reverseString(s)
print(s)
