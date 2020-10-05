import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructBTree(self, nums: list) -> TreeNode:
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
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
                if index == len(nums):
                    return root

    def helper(self, node: TreeNode):
        if not node:
            return 0
        res = node.val + self.helper(node.left) + self.helper(node.right)
        self.nodesSum.add(res)
        return res

    def maxProduct(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.nodesSum = set()
        sumNode = self.helper(root)
        maxSum = -float('inf')
        for tmp in self.nodesSum:
            maxSum = max(maxSum, (sumNode - tmp) * tmp)

        return maxSum % 1000000007


nums = [1, 1]
test = Solution()
root = test.constructBTree(nums)
print(test.maxProduct(root))
