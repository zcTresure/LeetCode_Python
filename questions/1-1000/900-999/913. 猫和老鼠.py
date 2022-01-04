# -*- coding: utf-8 -*-
# File:      913. 猫和老鼠.py
# DATA:      2022/1/4
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    DRAW = 0
    MOUSE_WIN = 1
    CAT_WIN = 2

    # 动态规划
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[[-1] * (n * 2) for _ in range(n)] for _ in range(n)]

        def getResult(mouse: int, cat: int, turns: int) -> int:
            if turns == n * 2:  # 轮次过多，则说明为平局
                return self.DRAW
            res = dp[mouse][cat][turns]
            if res != -1:  #
                return res
            if mouse == 0:  # 老鼠先到达 0 点，老鼠获胜
                res = self.MOUSE_WIN
            elif cat == mouse:  # 猫和老鼠在同一个位置，猫获胜
                res = self.CAT_WIN
            else:
                res = getNextResult(mouse, cat, turns)  # 进入下一轮
            dp[mouse][cat][turns] = res
            return res

        def getNextResult(mouse: int, cat: int, turns: int) -> int:
            curMove = mouse if turns % 2 == 0 else cat  # 奇数轮次是老鼠移动，偶数轮次是猫移动
            defaultRes = self.MOUSE_WIN if curMove != mouse else self.CAT_WIN  # 当前为猫移动时，默认结果为老鼠获胜
            res = defaultRes
            for next in graph[curMove]:
                if curMove == cat and next == 0:
                    continue
                nextMouse = next if curMove == mouse else mouse  # 当前为老鼠移动
                nextCat = next if curMove == cat else cat  # 当前为猫移动
                nextRes = getResult(nextMouse, nextCat, turns + 1)  # 下一轮次的结果
                if nextRes != defaultRes:  # 下一轮次的结果与默认结果不同
                    res = nextRes  # 更新结果
                    if res != self.DRAW:  # 结果不为平局，则直接结束游戏
                        break
            return res

        return getResult(1, 2, 0)


graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
print(Solution().catMouseGame(graph))
