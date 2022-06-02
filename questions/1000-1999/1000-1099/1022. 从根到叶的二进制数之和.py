# File Name:  1022. 从根到叶的二进制数之和
# date:       2021/3/29
# encode:      UTF-8
__author__ = 'zcTresure'

from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.helper(root)

    def helper(self, node, ret=0):
        if not node: return 0  # 空节点返回0
        ret = (ret << 1) + node.val  # 节点非空向右进1位
        if not node.left and not node.right:  # 叶子节点返回
            return ret
        # 递归左右子树
        return self.helper(node.left, ret) + self.helper(node.right, ret)


nums = [1, 0]
test = Solution()
root = BinaryTree.build(nums)
print(test.sumRootToLeaf(root))
