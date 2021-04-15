# File Name:  1600. 皇位继承顺序
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import defaultdict
from typing import List


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.dead_set = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead_set.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.res = []

        def dfs_NLR(king: str) -> None:  # N叉树的，前序遍历
            if king not in self.dead_set:
                self.res.append(king)
            for child in self.children[king]:
                dfs_NLR(child)

        dfs_NLR(self.king)
        return self.res

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
