# Date:       2021/3/31
# Coding:      UTF-8
__author__ = "zcTresure"


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

    # 先序遍历
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.count = 0  # 记录伪回文数

        def dfs(node, record=0):  # record 位运算初始记录为零
            if node:
                record ^= (1 << node.val)  # 将 1 右移 node.val 位，记录 node.val 出现的次数 1<=val<=8
                dfs(node.left, record)  # 递归调用左子树
                dfs(node.right, record)  # 递归调用归右子树
                if not node.left and not node.right:  # 为叶子节点判断是否为伪回文
                    if bin(record).count('1') < 2:  # 只有 record 中 1 出现的次数少于 2 才是伪回文 回文中心最多只有一个
                        self.count += 1  # 伪回文数加 1

        dfs(root)
        return self.count


nums = [8, 6, 9, None, None, None, 4, 4, 1, 5, 4, None, None, None, None, 8]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.pseudoPalindromicPaths(root))
