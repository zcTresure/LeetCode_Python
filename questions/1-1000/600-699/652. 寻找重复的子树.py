# File Name:  652. 寻找重复的子树
# date:       2021/4/12
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from template import BinaryTree
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = Counter()
        ans = []

        def collect(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans


nums = [1, 2, 3, 4, 2, 4, None, None, 4]
test = Solution()
root = BinaryTree.build(nums)
nodes = test.findDuplicateSubtrees(root)
for node in nodes:
    print(node.val)
