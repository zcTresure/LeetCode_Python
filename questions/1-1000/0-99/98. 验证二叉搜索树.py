# File Name:  98. 验证二叉搜索树
# date:       2021/3/30
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

    # 递归
    def isValidBST(self, root: TreeNode) -> bool:
        def heaper(node, lower=-float('inf'), upper=float('inf')):
            if not node: return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not heaper(node.left, lower, val):
                return False
            if not heaper(node.right, val, upper):
                return False
            return True

        return heaper(root)

    # 中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], -float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True


nums = [5, 1, 4, None, None, 3, 6]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.isValidBST(root))
