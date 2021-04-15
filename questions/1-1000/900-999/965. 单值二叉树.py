# File Name:  965. 单值二叉树
# date:       2021/4/2
# encode:      UTF-8
__author__ = 'zcTresure'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums:
            return TreeNode(-1)
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

    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        self.val = root.val

        def dfs(node):
            if not node: return True
            if node.val != self.val: return False
            L, R = dfs(node.left), dfs(node.right)
            return L and R

        return dfs(root)


nums = [1]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.isUnivalTree(root))
