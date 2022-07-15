# -*- coding: utf-8 -*-
# File:    558. 四叉树交集.py
# Date:    2022/7/15
# Software: Pycharm


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return Node(True, True, None, None, None, None) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return Node(True, True, None, None, None, None) if quadTree2.val else quadTree1
        tl, tr, bl, br = self.intersect(quadTree1.topLeft, quadTree2.topLeft), self.intersect(quadTree1.topRight,
                                                                                              quadTree2.topRight), self.intersect(
            quadTree1.bottomLeft, quadTree2.bottomLeft), self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        return Node(tl.val, True, None, None, None,
                    None) if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val else Node(
            False, False, tl, tr, bl, br)
