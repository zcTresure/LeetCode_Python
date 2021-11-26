# File Name:  1372. 二叉树中的最长交错路径
# date:       2021/3/30
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque, defaultdict
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        l, r = defaultdict(int), defaultdict(int)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                l[node.left] = r[node] + 1  # 树的左子树存在,左子树的路径继承右子树时父节点的值
                q.append(node.left)
            if node.right:
                r[node.right] = l[node] + 1  # 树的右子树存在,右子树的路径继承左子树时父节点的值
                q.append(node.right)
        res = 0
        for _, val in l.items():
            res = max(res, val)  # 找到左子树最长交错路径
        for _, val in r.items():
            res = max(res, val)  # 找到右子树最长交错路径
        return res

    def longestZigZag(self, root: TreeNode) -> int:
        maxans = 0

        def dfs(o, direction, length):
            if not o:
                return
            nonlocal maxans
            maxans = max(maxans, length)
            if direction == 0:
                dfs(o.left, 1, length + 1)
                dfs(o.right, 0, 1)
            else:
                dfs(o.right, 0, length + 1)
                dfs(o.left, 1, 1)

        dfs(root, 0, 0)
        dfs(root, 1, 0)
        return maxans


# nums = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, 1, None, 1, None, 1, None, 1]
nums = [1, None, 1, None, 1, None, 1, None, 1]
test = Solution()
root = BinaryTree.build(nums)
print(test.longestZigZag(root))
