# File Name:  987. 二叉树的垂序遍历
# date:       2021/4/13
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from template import BinaryTree
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        seen = defaultdict(lambda: defaultdict(list))

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node.val)
                dfs(node.left, x - 1, y + 1)  # 将二维二叉树向下压缩为一维坐标
                dfs(node.right, x + 1, y + 1)

        dfs(root)
        result = []
        for x in sorted(seen):
            tmp = []
            for y in sorted(seen[x]):
                tmp.extend(sorted(seen[x][y]))
            result.append(tmp)
        return result


nums = [15, 9, 20, None, None, 3, 7]
test = Solution()
root = BinaryTree.build(nums)
print(test.verticalTraversal(root))
