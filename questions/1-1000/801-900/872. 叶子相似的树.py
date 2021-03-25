# # File Name:  872. 叶子相似的树
# # date:       2021/3/24
# # encode:      UTF-8
# __author__ = 'zcTresure'

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return None
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def preOrder(root: TreeNode):
            if root:
                if not root.left and not root.right:
                    yield root.val
                yield from preOrder(root.left)
                yield from preOrder(root.right)

        return list(preOrder(root1)) == list(preOrder(root2))


nums1 = [1]
nums2 = [2]
test = Solution()
root1 = test.buildBinaryTree(nums1)
root2 = test.buildBinaryTree(nums2)
print(test.leafSimilar(root1, root2))
