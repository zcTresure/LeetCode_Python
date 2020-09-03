class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub = ''.join(ch.lower() for ch in s if ch.isalnum())
        return sub == sub[::-1]


s = "A man, a plan, a canal: Panama"
test = Solution()
print(test.isPalindrome(s))
