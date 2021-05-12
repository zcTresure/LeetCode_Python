# File Name:  1310. 子数组异或查询
# date:       2021/5/12
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cur = 0
        result, tmp = [], {}
        for i, val in enumerate(arr):
            cur ^= val
            tmp[i] = cur  # 记录0-n累计异或结果
        for l, r in queries:
            if l == 0:  # 左端为0，直接输出右端累计结果
                result.append(tmp[r])
            else:  # 左端不为0，右端异或左端就是区间异或结果
                result.append(tmp[l - 1] ^ tmp[r])
        return result


arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
test = Solution()
print(test.xorQueries(arr, queries))
