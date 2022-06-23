class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

    # 位运算
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        print(x, y)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


a = "1010"
b = "1011"
test = Solution()
print(test.addBinary(a, b))
