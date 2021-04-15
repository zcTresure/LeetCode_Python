# File Name:  589. N 叉树的前序遍历
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, ans = [root, ], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[::-1])
        return ans
