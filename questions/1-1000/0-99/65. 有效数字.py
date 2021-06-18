# -*- coding: utf-8 -*-
# File:     65. 有效数字.py
# Date:     2021/6/17
# Software: PyCharm
__author__ = 'zcFang'


class Solution:
    def isNumber(self, s: str) -> bool:
        # DFA transitions: dict[action] -> successor
        states = [{},  # state 1
                  {"blank": 1, "sign": 2, "digit": 3, "dot": 4},  # state 2
                  {"digit": 3, "dot": 4},  # state 3
                  {"digit": 3, "dot": 5, "e|E": 6, "blank": 9},  # state 4
                  {"digit": 5},  # state 5
                  {"digit": 5, "e|E": 6, "blank": 9},  # state 6
                  {"sign": 7, "digit": 8},  # state 7
                  {"digit": 8},  # state 8
                  {"digit": 8, "blank": 9},  # state 9
                  {"blank": 9}]

        def strToAction(st):
            if '0' <= st <= '9': return "digit"
            if st in "+-": return "sign"
            if st in "eE": return "e|E"
            if st == '.': return "dot"
            if st == ' ': return "blank"
            return None

        currState = 1
        for c in s:
            action = strToAction(c)
            if action not in states[currState]:
                return False
            currState = states[currState][action]

        # ending states: 3,5,8,9
        return currState in {3, 5, 8, 9}


print(Solution().isNumber('0.1'))
