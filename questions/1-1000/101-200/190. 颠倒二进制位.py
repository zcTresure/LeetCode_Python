class Solution:
    # 逐位颠倒
    def reverseBits(self, n: int) -> int:
        res, b = 0, 31
        while n:
            res += (n & 1) << b
            n >>= 1
            b -= 1
        return res

    # 带记忆化的按字节颠倒
    def reverseBits(self, n):
        ret, power = 0, 24
        cache = dict()
        while n:
            ret += self.reverseByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ret

    def reverseByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
        return cache[byte]


test = Solution()
print(test.reverseBits(43261596))
