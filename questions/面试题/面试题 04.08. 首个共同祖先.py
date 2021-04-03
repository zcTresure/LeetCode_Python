# File Name:  面试题 04.08. 首个共同祖先
# date:       2021/4/3
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

    def findVal(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val == val: return root
        self.findVal(root.left, val)
        self.findVal(root.right, val)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == q or root == p: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        return left if left else right


nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
test = Solution()
root = test.buildBinaryTree(nums)
node_p = test.findVal(root, p)
node_q = test.findVal(root, q)
print(node_q)
print(node_q)
print(test.lowestCommonAncestor(root, node_p, node_q).val)
