# File Name:  1022. 从根到叶的二进制数之和
# date:       2021/3/29
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

    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.heaper(root)

    def heaper(self, node, ret=0):
        if not node: return 0  # 空节点返回0
        ret = (ret << 1) + node.val  # 节点非空向右进1位
        if not node.left and not node.right:  # 叶子节点返回
            return ret
        # 递归左右子树
        return self.heaper(node.left, ret) + self.heaper(node.right, ret)


nums = [1, 0]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.sumRootToLeaf(root))
