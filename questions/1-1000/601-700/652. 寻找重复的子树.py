# File Name:  652. 寻找重复的子树
# date:       2021/4/12
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums:
            return TreeNode(-1)
        root = TreeNode(nums[0])
        nodes, index, n = [root], 1, len(nums)
        for node in nodes:
            if node != None:
                if index == n:
                    return root
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.left)
                index += 1
                if index == n:
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.right)
                index += 1

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
root = test.buildBinaryTree(nums)
nodes = test.findDuplicateSubtrees(root)
for node in nodes:
    print(node.val)
