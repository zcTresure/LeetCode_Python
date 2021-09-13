# File Name:  1008. 前序遍历构造二叉搜索树
# date:       2021/4/14
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> None:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                print(node.val, end='')
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if q:
                    print(end=' ')
        print()

    # 递归
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.index = 0

        def dfs(lower, upper):
            if self.index == len(preorder) or preorder[self.index] > upper or preorder[self.index] < lower:
                return
            mid = preorder[self.index]
            node = TreeNode(mid)
            self.index += 1
            node.left = dfs(lower, mid)
            node.right = dfs(mid, upper)
            return node

        return dfs(float('-inf'), float('inf'))

    # 迭代
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        stack = list()
        for val in preorder:
            node = TreeNode(val)
            if not root:
                root = node
                stack.append(root)
                continue
            if stack[-1].val > node.val:
                stack[-1].left = node
            else:
                pre_node = stack.pop()
                while stack and stack[-1].val < node.val:
                    pre_node = stack.pop()
                pre_node.right = node
            stack.append(node)

        return root


nums = [8, 5, 1, 7, 10, 12]
test = Solution()
root = test.bstFromPreorder(nums)
test.levelOrder(root)
