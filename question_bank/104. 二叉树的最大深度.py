# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 深度优先搜索
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height)


# 深度优先搜索另一种写法
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 广度优先搜索
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        tmp, ret = [root], 1
        while tmp:
            ret, tmp = ret + \
                1, sum([([i.left] if i.left else []) +
                        ([i.right] if i.right else []) for i in tmp], [])
        return ret - 1


Tree = [3, 9, 20, null, null, 15, 7]
print(Solution.maxDepth(1, Tree))
