# File Name:  面试题 04.06. 后继者
# date:       2021/4/16
# encode:      UTF-8
__author__ = 'zcTresure'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums: return None
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

    # 查找目标值为target的节点
    def findNode(self, root: TreeNode, target: int) -> TreeNode:
        self.target_node = None

        def dfs(node):
            if node:
                if node.val == target:
                    self.target_node = node
                    return
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.target_node

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        pre = None
        while root.val != p.val:
            if root.val > p.val:  # 节点值大于目标节点值，向左查找，更新父节点
                pre = root
                root = root.left
            else:  # 节点值小于目标节点值，向右查找，父节点小于右孩子，不更新后继节点
                root = root.right
        if not root.right:  # 右孩子不存在，后继节点为父节点
            return pre
        else:
            root = root.right  # 右孩子存在，找到右孩子的最左节点
            while root.left:
                root = root.left
            return root


nums = [5, 3, 6, 2, 4, None, None, 1]
p = 3
test = Solution()
root = test.buildBinaryTree(nums)
target_p = test.findNode(root, p)
pre = test.inorderSuccessor(root, target_p)
print(pre.val if pre else None)
