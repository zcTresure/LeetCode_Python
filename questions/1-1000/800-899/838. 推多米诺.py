# -*- coding: utf-8 -*-
# File:      838. 推多米诺.py
# DATA:      2022/2/21
# Software:  PyCharm
__author__ = 'zcFang'

from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        q = deque()
        time = [-1] * n
        force = [[] for _ in range(n)]
        for i, f in enumerate(dominoes):
            if f != '.':
                q.append(i)
                time[i] = 0
                force[i].append(f)

        res = ['.'] * n
        while q:
            i = q.popleft()
            if len(force[i]) == 1:
                res[i] = f = force[i][0]
                ni = i - 1 if f == 'L' else i + 1
                if 0 <= ni < n:
                    t = time[i]
                    if time[ni] == -1:
                        q.append(ni)
                        time[ni] = t + 1
                        force[ni].append(f)
                    elif time[ni] == t + 1:
                        force[ni].append(f)
        return ''.join(res)

    # 模拟
    def pushDominoes(self, dominoes: str) -> str:
        ans = list(dominoes)
        left, i, n = 'L', 0, len(ans)
        while i < n:
            j = i
            while j < n and ans[j] == '.':
                j += 1
            right = ans[j] if j < n else 'R'
            if left == right:
                while i < j:
                    ans[i] = right
                    i += 1
            elif left == 'R' and right == 'L':
                k = j - 1
                while i < k:
                    ans[i] = 'R'
                    ans[k] = 'L'
                    i += 1
                    k -= 1
            left = right
            i = j + 1
        return "".join(ans)


print(Solution().pushDominoes(dominoes="RR.L"))
print(Solution().pushDominoes(dominoes=".L.R...LR..L.."))
