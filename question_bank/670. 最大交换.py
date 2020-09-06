class Solution:
    def maximumSwap(self, num: int) -> int:
        left_offset, max_digit = -1, -1
        tmp, offset = num, 1
        ret = num
        while tmp > 0:
            n = tmp % 10
            if n > max_digit:
                left_offset, max_digit = offset, n
            elif n < max_digit:
                ret = num + (max_digit - n) * (offset - left_offset)
            tmp = tmp // 10
            offset *= 10
        return ret


num = 12345698
test = Solution()
print(test.maximumSwap(num))
