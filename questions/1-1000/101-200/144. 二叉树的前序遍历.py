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

    # 先序遍历 递归
    def preorderTraversal(self, root: TreeNode) -> list:
        ans = []

        def preorderPrint(node: TreeNode) -> None:
            if not node:
                return
            ans.append(node.val)
            preorderPrint(node.left)
            preorderPrint(node.right)

        preorderPrint(root)
        return ans

    # 先序遍历 迭代
    def preorderTraversal(self, root: TreeNode) -> list:
        ans = []
        if not root:
            return ans
        stack = []
        node = root
        while stack or node:
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return ans

    # morris遍历
    def preorderTraversal(self, root: TreeNode) -> list:
        ans = []
        if not root:
            return ans
        pre = root
        while pre:
            cur = pre.left
            if cur:
                while cur.right and cur.right != pre:
                    cur = cur.right
                if not cur.right:
                    ans.append(pre.val)
                    cur.right = pre
                    pre = pre.left
                    continue
                else:
                    cur.right = None
            else:
                ans.append(pre.val)
            pre = pre.right
        return ans


nums = [1, None, 2, 3]
test = Solution()
root = test.constructBTree(nums)
ans = test.preorderTraversal(root)
print(ans)
