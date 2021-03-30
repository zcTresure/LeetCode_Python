# File Name:  剑指 Offer 28. 对称的二叉树
# date:       2021/3/29
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

    def isSymmetric(self, root: TreeNode) -> bool:
        def heaper(L, R):
            if not L and not R: return True  # 左节点和右节点都不存在，二叉树对称
            if not L or not R or L.val != R.val: return False
            # 递归检查左节点的左孩子和右节点的右孩子 或 左节点的右孩子和右节点的左孩子是否对称
            return heaper(L.left, R.right) and heaper(L.right, R.left)

        # 根节点为空时对称二叉树，否则递归检查左右子树
        return heaper(root.left, root.right) if root else True


nums = [1, 2, 2, 3, 4, 4, 3]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.isSymmetric(root))