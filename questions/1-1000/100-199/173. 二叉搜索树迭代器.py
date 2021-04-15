# File Name:  173. 二叉搜索树迭代器
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [(root, 0)]

    def next(self) -> int:
        while True:
            node, color = self.stack.pop()
            if color == 1:
                return node.val
            if node.right:
                self.stack.append((node.right, 0))
            self.stack.append((node, 1))
            if node.left:
                self.stack.append((node.left, 0))

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
