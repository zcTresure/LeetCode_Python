import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return TreeNode(-1)
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

    def levelorderPrint(self, root: TreeNode) -> None:
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.val, end='')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if q:
                print(end=' ')
        print()

    def sumNumbers(self, root: TreeNode) -> int:
        def preorder(node: TreeNode, tmp: int):
            nonlocal res
            if not node:
                res += tmp // 2
                return
            tmp = tmp * 10 + node.val
            # if not node.left and not node.right:
            #     res += tmp
            #     return
            preorder(node.left, tmp)
            preorder(node.right, tmp)

        res = 0
        preorder(root, 0)
        return res


nums = []
test = Solution()
root = test.buildTree(nums)
test.levelorderPrint(root)
print(test.sumNumbers(root))
