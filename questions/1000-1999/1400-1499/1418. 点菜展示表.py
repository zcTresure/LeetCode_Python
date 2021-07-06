# -*- coding: utf-8 -*-
# File:      1418. 点菜展示表.py
# DATA:      2021/7/6
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        res = list()
        foods = set()  # 定义食物的种类集合
        table_info = defaultdict(lambda: defaultdict(int))  # 定义嵌套哈希表
        for _, table, food in orders:
            table_info[table][food] += 1  # table_info 中桌号对应 食物名称 数量 +1
            foods.add(food)  # 添加食物的集合
        foods = sorted(foods)  # 对食物进行字典排序
        res.append(['Table'] + foods)  # 组装第一行
        for table_num in sorted(table_info, key=lambda x: int(x)):  # 根据 int(table) 排序后, 遍历
            tmp = [table_num]  # 第一列为桌号
            for food in foods:  # 循环遍历食物, 存在食物直接添加, 不存在添 0
                tmp.append(str(table_info.get(table_num).get(food, 0)))
            res.append(tmp)  # 添加该桌的数据
        return res


orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
          ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
tables = Solution().displayTable(orders)
for table in tables:
    print(table)
