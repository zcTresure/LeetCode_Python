# File Name:  671. 二叉树中第二小的节点
# date:       2021/4/12
# encode:      UTF-8
__author__ = 'zcTresure'

import heapq


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


nums = [1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 8]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.findSecondMinimumValue(root))
