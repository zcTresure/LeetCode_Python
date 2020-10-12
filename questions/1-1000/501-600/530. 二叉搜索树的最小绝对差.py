import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructBTree(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return None
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

    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        nums = []
        dfs(root)
        ans = float("inf")
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i - 1])
        return ans

    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            nonlocal pre, ans
            if not node:
                return
            dfs(node.left)
            if pre != -1:
                ans = min(ans, node.val - pre)
            pre = node.val
            dfs(node.right)

        pre, ans = -1, float("inf")
        dfs(root)
        return ans


nums = [236, 104, 701, None, 227, None, 911]
test = Solution()
root = test.constructBTree(nums)
print(test.getMinimumDifference(root))
