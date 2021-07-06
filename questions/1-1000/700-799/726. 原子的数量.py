# -*- coding: utf-8 -*-
# File:      726. 原子的数量.py
# DATA:      2021/7/5
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i, n = 0, len(formula)
        atom_cnt_depth, stack = [], []
        while i < n:
            atom = ''
            if formula[i].isupper():  # 原子
                atom += formula[i]
                i += 1
                while i < n and formula[i].islower():
                    atom += formula[i]
                    i += 1
            if atom:  # 原子次数
                cnt = 0
                if i < n and formula[i].isdigit():
                    while i < n and formula[i].isdigit():
                        cnt = cnt * 10 + int(formula[i])
                        i += 1
                else:
                    cnt = 1
                atom_cnt_depth.append([atom, cnt, len(stack)])
            if i < n and formula[i] == '(':
                stack.append('(')
                i += 1
            elif i < n and formula[i] == ')':
                i += 1
                cnt = 0
                if i < n and formula[i].isdigit():
                    while i < n and formula[i].isdigit():
                        cnt = cnt * 10 + int(formula[i])
                        i += 1
                else:
                    cnt = 1
                for j in range(len(atom_cnt_depth) - 1, -1, -1):
                    if atom_cnt_depth[j][2] == len(stack):  # 是当前的深度
                        atom_cnt_depth[j][1] *= cnt  # 字母复制
                        atom_cnt_depth[j][2] -= 1  # 深度-1
                    else:
                        break
                stack.pop(-1)
        atom_freq = defaultdict()
        for name, cnt, depth in atom_cnt_depth:
            if name not in atom_freq:
                atom_freq[name] = 0
            atom_freq[name] += cnt

        res = ""
        for atom, freq in sorted(atom_freq.items()):
            res += atom
            if freq > 1:
                res += str(freq)
        return res

    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        atom_cnt_depth = []  # 原子-频率-括号深度
        DEPTH = i = 0  # 每到一处，左括号的个数就是当前name的深度
        while i < n:
            # （1）找原子
            atom = ""
            if formula[i].isupper() == True:  # 大写字母开头
                atom += formula[i]
                i += 1
                while i < n and formula[i].islower():
                    atom += formula[i]
                    i += 1

            # （2）原子后面是次数
            if atom != '':
                cnt = 0
                if i < n and formula[i].isdigit() == True:  # 如果atom后面有数字
                    while i < n and formula[i].isdigit() == True:
                        cnt = cnt * 10 + int(formula[i])
                        i += 1
                else:  # 若atom后面没数字
                    cnt = 1
                atom_cnt_depth.append([atom, cnt, DEPTH])

            # （3）括号的情况
            if i < n and formula[i] == '(':
                DEPTH += 1
                i += 1
            elif i < n and formula[i] == ')':
                i += 1
                cnt = 0
                # 后面有数字
                if i < n and formula[i].isdigit() == True:
                    while i < n and formula[i].isdigit() == True:
                        cnt = cnt * 10 + int(formula[i])
                        i += 1
                else:  # 后面不是数字
                    cnt = 1

                # (4)')'后面的倍数
                for j in range(len(atom_cnt_depth) - 1, -1, -1):
                    if atom_cnt_depth[j][2] == DEPTH:  # 是当前的深度
                        atom_cnt_depth[j][1] *= cnt  # 字母复制
                        atom_cnt_depth[j][2] -= 1  # 深度-1
                    else:
                        break
                DEPTH -= 1  # 当前深度的都计算好了,深度可以-1了

        atom_freq = defaultdict()
        for atom, cnt, depth in atom_cnt_depth:
            if atom not in atom_freq:
                atom_freq[atom] = 0
            atom_freq[atom] += cnt

        res = ""
        for atom, freq in sorted(atom_freq.items()):
            res += atom
            if freq > 1:
                res += str(freq)
        return res


# formula = 'H2O'
# formula = "Mg(OH)2"
formula = "K4(ON(SO3)2)2"
print(Solution().countOfAtoms(formula))
