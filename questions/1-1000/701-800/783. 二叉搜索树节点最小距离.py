# File Name:  783. 二叉搜索树节点最小距离
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
    def constructBTree(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return TreeNode()
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                if index == len(nums):
                    return root
                node.left = TreeNode(
                    nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(
                    nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1

    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            nonlocal pre, ans
            if not node:
                return
            dfs(node.left)
            if pre != -1:
                ans = min(ans, node.val - pre)
            pre = node.val
            dfs(node.right)

        pre, ans = -1, 100000
        dfs(root)
        return ans


nums = [236, 104, 701, None, 227, None, 911]
test = Solution()
root = test.constructBTree(nums)
print(test.minDiffInBST(root))
