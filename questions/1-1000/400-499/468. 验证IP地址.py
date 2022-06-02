# -*- coding: utf-8 -*-
# File:      468. 验证IP地址.py
# DATA:      2022/5/29
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        n = len(queryIP)
        if '.' in queryIP:
            # 点个数
            cnt = 0
            addr = 0
            for i in range(n):
                if queryIP[i].isdigit():
                    # 数字首位不能为零
                    if addr == int(queryIP[i]) == 0 and i != n - 1 and queryIP[i + 1].isdigit():
                        return "Neither"
                    # 数字累计
                    addr = addr * 10 + int(queryIP[i])
                elif queryIP[i] == '.':
                    # 点前一位必为数字，点前数字不能超过255
                    if not queryIP[i - 1].isdigit() or addr > 255:
                        return "Neither"
                    addr = 0
                    cnt += 1
                else:
                    return "Neither"
            # IPv4冒号为3个，长度大于7，最后一个数字判定
            return "IPv4" if cnt == 3 and n >= 7 and addr <= 255 else "Neither"
        else:
            # 冒号个数
            cnt = 0
            ip = ""
            addr = []
            for c in queryIP:
                # IPv6地址码记录
                if c in "0123456789abcdefABCDEF":
                    ip = ip + c
                elif c == ":":
                    cnt += 1
                    addr.append(ip)
                    # IPv6地址码位数不超过四个
                    if len(ip) > 4:
                        return "Neither"
                    ip = ""
                else:
                    return "Neither"
            addr.append(ip)
            # IPv6冒号七个所有地址码长度在 1-4 之间
            return "IPv6" if cnt == 7 and all([1 <= len(ip) <= 4 for ip in addr]) else "Neither"


queryIP = ["0.0.0.256"]
ans = []
for ip in queryIP:
    ans.append(Solution().validIPAddress(ip))
print(ans)
