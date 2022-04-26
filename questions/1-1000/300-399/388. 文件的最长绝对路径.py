# -*- coding: utf-8 -*-
# File:      388. 文件的最长绝对路径.py
# DATA:      2022/4/20
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        manu = []
        ans, i, n = 0, 0, len(input)
        while i < n:
            depth = 1
            while i < n and input[i] == '\t':  # 检测当前文件深度
                depth += 1
                i += 1

            length, is_file = 0, False
            while i < n and input[i] != '\n':  # 检测当前文件长度
                if input[i] == '.':
                    is_file = True
                length += 1
                i += 1
            i += 1  # 跳过换行符

            while len(manu) >= depth:  # 确定当前文件路径
                manu.pop()
            if manu:
                length += manu[-1] + 1
            if is_file:  # 当前是文件
                ans = max(ans, length)
            else:  # 当前是目录
                manu.append(length)
        return ans


print(Solution().lengthLongestPath(input="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print(Solution().lengthLongestPath(
    input="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
