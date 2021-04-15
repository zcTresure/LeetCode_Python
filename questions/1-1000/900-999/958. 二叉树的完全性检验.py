# File Name:  958. 二叉树的完全性检验
# date:       2021/4/6
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

    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]  # 记录完全二叉树的节点数
        index = 0
        while index < len(nodes):
            node, count = nodes[index]
            index += 1
            if node:
                nodes.append((node.left, count * 2))  # 左孩子为父节点的两倍
                nodes.append((node.right, count * 2 + 1))  # 右孩子为父节点两倍多一个
        return nodes[-1][1] == len(nodes)  # nodes的长度就是树节点的个数，如果为完全二叉树，则等式成立


nums = [1, 2, 3, 4, 5, None, 7]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.isCompleteTree(root))
