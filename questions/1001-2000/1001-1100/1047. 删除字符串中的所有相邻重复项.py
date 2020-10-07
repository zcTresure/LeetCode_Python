from string import ascii_lowercase


class Solution:
    def removeDuplicates(self, S: str) -> str:
        duplicates = {2 * ch for ch in ascii_lowercase}
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
        return S

    def removeDuplicates(self, S: str) -> str:
        result = list(' ')
        for c in S:
            if c == result[-1]:
                result.pop()
            else:
                result.append(c)
        return ''.join(result[1:])


S = "abbaca"
print(Solution().removeDuplicates(S))
