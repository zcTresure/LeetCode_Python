# File Name:  671. 二叉树中第二小的节点
# date:       2021/4/12
# encode:      UTF-8
__author__ = 'zcTresure'

import heapq
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        result = set()

        def heaper(node):
            if node:
                result.add(node.val)
                heaper(node.left)
                heaper(node.right)

        heaper(root)
        result = list(result)
        heapq.heapify(result)
        heapq.heappop(result)
        return -1 if not result else result[0]

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans, root_val = -1, root.val

        def dfs(node: TreeNode) -> None:
            nonlocal ans
            if not node:
                return
            if ans != -1 and node.val >= ans:  # 剪枝
                return
            if node.val > root_val:
                ans = node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans


nums = [1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 8]
test = Solution()
root = BinaryTree.build(nums)
print(test.findSecondMinimumValue(root))
