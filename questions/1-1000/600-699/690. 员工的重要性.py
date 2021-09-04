# -*- coding: utf-8 -*-
# File:      690. 员工的重要性.py
# DATA:      2021/9/3
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], idx: int) -> int:
        mp = {employee.id: employee for employee in employees}

        def dfs(idx: int) -> int:
            employee = mp[idx]
            total = employee.importance + sum(dfs(subIdx) for subIdx in employee.subordinates)
            return total

        return dfs(idx)


employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
idx = 1
print(Solution.getImportance(employees, idx))
