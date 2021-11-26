# File Name:  958. 二叉树的完全性检验
# date:       2021/4/6
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
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]  # 记录完全二叉树的节点数
        index = 0
        while index < len(nodes):
            node, count = nodes[index]
            index += 1
            if node:
                nodes.append((node.left, count * 2))  # 左孩子为父节点的两倍
                nodes.append((node.right, count * 2 + 1))  # 右孩子为父节点两倍多一个
        return nodes[-1][1] == len(nodes)  # nodes的长度就是树节点的个数，如果为完全二叉树，则等式成立


nums = [1, 2, 3, 4, 5, None, 7]
test = Solution()
root = BinaryTree.build(nums)
print(test.isCompleteTree(root))
