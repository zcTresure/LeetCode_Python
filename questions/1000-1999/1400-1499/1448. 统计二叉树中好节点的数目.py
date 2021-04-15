# File Name:  1448. 统计二叉树中好节点的数目
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0

        def dfs(node, max_value=float("-inf")):
            if not node: return
            if node.val >= max_value:
                self.result += 1
                max_value = node.val
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root)
        return self.result


nums = [3, 1, 4, 3, None, 1, 5]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.goodNodes(root))
