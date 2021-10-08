# -*- coding: utf-8 -*-
# File:      482. 密钥格式化.py
# DATA:      2021/10/8
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = list()
        cnt = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                ans.append(s[i].upper())
                cnt += 1
                if cnt % k == 0:
                    ans.append("-")

        if ans and ans[-1] == "-":
            ans.pop()

        return "".join(ans[::-1])


S = "5F3Z-2e-9-w"
K = 4
print(Solution().licenseKeyFormatting(S, K))
