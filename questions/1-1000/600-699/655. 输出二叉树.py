# File Name:  655. 输出二叉树
# date:       2021/4/12
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        heigh = self.getHeight(root)
        result = [[""] * ((1 << heigh) - 1) for _ in range(heigh)]  # 矩阵的宽度为树最深一层的最大宽度
        self.fill(result, root, 0, 0, len(result[0]))
        return result

    def fill(self, result: list, root: TreeNode, i, left, right):
        if not root: return
        result[i][(left + right) // 2] = str(root.val)
        self.fill(result, root.left, i + 1, left, (left + right) // 2)
        self.fill(result, root.right, i + 1, (left + right + 1) // 2, right)

    # 二叉树的深度
    def getHeight(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


nums = [1, 2, 5, 3, None, None, None, 4]
test = Solution()
root = BinaryTree.build(nums)
result = test.printTree(root)
for i in range(len(result)):
    print(result[i])
