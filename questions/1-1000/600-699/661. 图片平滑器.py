# -*- coding: utf-8 -*-
# File:      661. 图片平滑器.py
# DATA:      2022/3/24
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total, num = 0, 0
                for x in range(max(i - 1, 0), min(i + 2, m)):
                    for y in range(max(j - 1, 0), min(j + 2, n)):
                        total += img[x][y]
                        num += 1
                ans[i][j] = total // num

        return ans


img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
print(Solution().imageSmoother(img))
