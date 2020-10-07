class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res, writeA = '', False
        while A or B:
            print(A, B)
            if len(res) >= 2 and res[-1] == res[-2]:
                writeA = res[-1] == 'b'
            else:
                writeA = A >= B
            if writeA:
                res += 'a'
                A -= 1
            else:
                res += 'b'
                B -= 1
        return res

    def strWithout3a3b(self, A: int, B: int) -> str:
        if A + B >= 3:
            if A > B:
                return "aab" + self.strWithout3a3b(A - 2, B - 1)
            elif A < B:
                return "bba" + self.strWithout3a3b(A - 1, B - 2)
            else:
                return 'ab' * A
        else:
            return 'a' * A + 'b' * B


test = Solution()
print(test.strWithout3a3b(4, 2))
