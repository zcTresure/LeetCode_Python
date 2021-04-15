# File Name:  979. 在二叉树中分配硬币
# date:       2021/4/1
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

    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node):
            if not node: return 0
            # L, R 表示左子树和右子树的过载量，有正有负，负数表示要移动硬币到该结点，正数是要从该结点移出硬币
            L, R = dfs(node.left), dfs(node.right)
            self.res += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.res


nums = [1, 0, 0, None, 3]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.distributeCoins(root))
