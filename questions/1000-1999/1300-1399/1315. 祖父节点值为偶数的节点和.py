# File Name:  1315. 祖父节点值为偶数的节点和
# date:       2021/4/2
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(grandparent, parent, node):
            if not node: return
            if grandparent % 2 == 0:  # 祖父值为偶数，节点值加入答案
                self.ans += node.val
            dfs(parent, node.val, node.left)  # 递归调用左子树
            dfs(parent, node.val, node.right)  # 递归调用右子树

        dfs(1, 1, root)
        return self.ans

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = deque([root])
        ans = 0
        while len(q) > 0:
            node = q.popleft()
            if node.val % 2 == 0:  # 值为偶数
                if node.left:
                    if node.left.left:  # 孙子节点存在，则加入答案
                        ans += node.left.left.val
                    if node.left.right:
                        ans += node.left.right.val
                if node.right:
                    if node.right.left:
                        ans += node.right.left.val
                    if node.right.right:
                        ans += node.right.right.val
            if node.left:  # 孩子节点入队列
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans


nums = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
test = Solution()
root = BinaryTree.build(nums)
print(test.sumEvenGrandparent(root))
