class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        res = ''
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return '1' + res if carry else res


num1 = '123456789'
num2 = '987654321'
print(Solution.addStrings(1, num1, num2))
