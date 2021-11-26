# File Name:  112. 路径总和
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 先序遍历
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    # 广度优先搜索
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        queue_node = deque([root])
        queue_val = deque([root.val])
        while queue_node:
            node = queue_node.popleft()
            path_val = queue_val.popleft()
            if not node.left and not node.right:
                if path_val == targetSum:
                    return True
                continue
            if node.left:
                queue_node.append(node.left)
                queue_val.append(node.left.val + path_val)
            if node.right:
                queue_node.append(node.right)
                queue_val.append(node.right.val + path_val)
        return False

    # # 递归
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


nums = [-2, None, -3]
targetSum = -2
test = Solution()
root = BinaryTree.build(nums)
test.preOrder(root)
print(test.hasPathSum(root, targetSum))
