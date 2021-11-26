# File Name:  572. 另一个树的子树
# date:       2021/4/12
# encode:      UTF-8
__author__ = 'zcTresure'

from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check(s, t):
            if not s and not t: return True
            if not s or not t or s.val != t.val:
                return False
            return check(s.left, t.left) and check(s.right, t.right)

        def dfs(s, t):
            if not s:
                return False
            return check(s, t) or dfs(s.left, t) or dfs(s.right, t)

        return dfs(s, t)


node1 = [3, 4, 5, 1, 2]
node2 = [4, 1, 2]
test = Solution()
s = BinaryTree.build(node1)
t = BinaryTree.build(node2)
print(test.isSubtree(s, t))
