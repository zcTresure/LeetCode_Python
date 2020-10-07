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

    def postorderTraversal(self, root: TreeNode) -> list:
        def dfs(root: TreeNode):
            if root:
                dfs(root.left)
                dfs(root.right)
                ans.append(root.val)
        ans = []
        dfs(root)
        return ans

    def postorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        ans, stack, prev = [], [], None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                ans.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return ans

    def postorderTraversal(self, root: TreeNode) -> list:
        def addPath(node: TreeNode):
            tmp = list()
            while node:
                tmp.append(node.val)
                node = node.right
            res.extend(tmp[::-1])
        if not root:
            return list()
        res = list()
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
                    addPath(p1.left)
            p1 = p1.right
        addPath(root)
        return res


nums = [1, None, 2, 3]
test = Solution()
root = test.constructBTree(nums)
print(test.postorderTraversal(root))
