# File Name:  700. 二叉搜索树中的搜索
# date:       2021/4/13
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

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.node = None

        def dfs(node):
            if not node: return
            if node.val == val:
                self.node = node
                return
            elif node.val > val:
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)
        return self.node


nums = [4, 2, 7, 1, 3]
val = 2
test = Solution()
root = test.buildBinaryTree(nums)
node = test.searchBST(root, val)
print(node.val) if node else print(0)
