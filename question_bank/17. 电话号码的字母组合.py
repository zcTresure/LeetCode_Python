class Solution:
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        number_dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                      "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index: int) -> None:
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in number_dic[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


digits = '23'
test = Solution()
print(test.letterCombinations(digits))
