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

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node: TreeNode, point=None):
            if node:
                depth[node.val] = 1 + depth[point.val] if point else 0
                parent[node.val] = point
                dfs(node.left, node)
                dfs(node.right, node)

        parent = {}
        depth = {}
        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]


nums = [1, 2, 5, 3, None, None, 6, 4]
x = 6
y = 3
test = Solution()
root = test.constructBTree(nums)
print(test.isCousins(root, x, y))
