# File Name:  N 叉树
# date:       2021/4/13
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(node) for node in root.children]
            return max(height) + 1

    def maxDepth(self, root: 'Node') -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))

        return depth
