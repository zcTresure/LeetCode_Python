# -*- coding: utf-8 -*-
# File:      587. 安装栅栏.py
# DATA:      2022/4/23
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees
        left_most = 0
        for i, tree in enumerate(trees):
            if tree[0] < left_most:
                left_most = i
        ans = []
        visited = [False] * n
        p = left_most
        while True:
            q = (p + 1) % n
            for r, tree in enumerate(trees):
                # 如果 r 在 pq 的右侧，则 q = r
                if cross(trees[p], trees[q], trees[r]):
                    q = r
            # 是否存在点 i，使得p q i 在同一条直线上
            for i, b in enumerate(visited):
                if not b and i != p and i != q and cross(trees[p], trees[q], trees[i]) == 0:
                    ans.append(trees[i])
                    visited[i] = True
            if not visited[q]:
                ans.append(trees[q])
            p = q
            if p == left_most:
                break
        return ans

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        def distance(p: List[int], q: List[int]) -> int:
            return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

        n = len(trees)
        if n < 4:
            return trees
        bottom = 0
        for i, tree in enumerate(trees):
            if tree[1] < trees[bottom][1]:
                bottom = i
        trees[bottom], trees[0] = trees[0], trees[bottom]

        def cmp(a: List[int], b: List[int]) -> int:
            diff = cross(trees[0], b, a) - cross(trees[0], a, b)
            return diff if diff else distance(trees[0], a) - distance(trees[0], b)

        trees[1:] = sorted(trees[1:], key=cmp_to_key(cmp))

        # 对于凸包最后且在同一条直线的元素按照距离从小到大进行排序
        r = n - 1
        while r >= 0 and cross(trees[0], trees[n - 1], trees[r]) == 0:
            r -= 1
        l, h = r + 1, n - 1
        while l < h:
            trees[l], trees[h] = trees[h], trees[l]
            l += 1
            h -= 1

        stack = [0, 1]
        for i in range(2, n):
            # 如果当前元素与栈顶的两个元素构成的向量顺时针旋转，则弹出栈顶元素
            while len(stack) > 1 and cross(trees[stack[-2]], trees[stack[-1]], trees[i]) < 0:
                stack.pop()
            stack.append(i)
        return [trees[i] for i in stack]

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        # 按照 x 从小到大排序，如果 x 相同，则按照 y 从小到大排序
        trees.sort()

        hull = [0]  # hull[0] 需要入栈两次，不标记
        used = [False] * n
        # 求凸包的下半部分
        for i in range(1, n):
            while len(hull) > 1 and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                used[hull.pop()] = False
            used[i] = True
            hull.append(i)
        # 求凸包的上半部分
        m = len(hull)
        for i in range(n - 2, -1, -1):
            if not used[i]:
                while len(hull) > m and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                    used[hull.pop()] = False
                used[i] = True
                hull.append(i)
        # hull[0] 同时参与凸包的上半部分检测，因此需去掉重复的 hull[0]
        hull.pop()

        return [trees[i] for i in hull]


print(Solution().outerTrees(trees=[[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]))
