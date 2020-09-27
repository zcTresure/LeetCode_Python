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

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getPath(root: TreeNode, target: TreeNode) -> list:
            path = list()
            node = root
            while node != target:
                path.append(node)
                if target.val > node.val:
                    node = node.right
                else:
                    node = node.left
            path.append(node)
            return path

        pPath = getPath(root, p)
        qPath = getPath(root, q)
        ancestor = None
        for x, y in zip(pPath, qPath):
            if x == y:
                ancestor = x
            else:
                break
        return ancestor


nums = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p, q = 2, 8
test = Solution()
root = test.constructBTree(nums)
