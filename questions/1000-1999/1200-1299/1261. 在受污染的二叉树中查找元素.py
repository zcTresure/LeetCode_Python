# Date:       2021/4/1
# Coding:      UTF-8
__author__ = "zcTresure"

from template import BinaryTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    # 先序遍历
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)


class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        self.dic = set()

        def dfs(node):
            self.dic.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                dfs(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                dfs(node.right)

        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.dic

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
