# File Name:  面试题 04.09. 二叉搜索树序列
# date:       2021/4/15
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
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root: return [[]]
        result = []

        def findPath(node, tmp, path):
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.right)
            if not tmp:
                result.append(path[:])
                return
            for i, next in enumerate(tmp):
                new_tmp = tmp[:i] + tmp[i + 1:]  # 去除二叉树的根节点
                findPath(next, new_tmp, path + [next.val])

        findPath(root, [], [root.val])
        return result


nums = [2, 1, 3]
test = Solution()
root = BinaryTree.build(nums)
result = test.BSTSequences(root)
for tmp in result:
    print(tmp)
