# File Name:  230. 二叉搜索树中第K小的元素
# date:       2021/4/2
# encode:      UTF-8
__author__ = 'zcTresure'


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

    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        return inorder(root)[k - 1]

    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


nums = [4, 2, 5, 3]
k = 1
test = Solution()
root = test.buildBinaryTree(nums)
print(test.kthSmallest(root, k))
