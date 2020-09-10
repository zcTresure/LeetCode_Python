class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ans = ""
        stack = []
        index = 0
        while index < len(s):
            j = index
            while j < len(s) and s[j] != ' ':
                j += 1
            stack.append(s[index:j])
            index = j+1
        while stack:
            ans += stack.pop() + " "
        return ans[:-1]

    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


s = "  hello world!  "
print(Solution().reverseWords(s))       