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

    # 先序遍历
    def preorderTraversal(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preorderPrint(root.left)
        self.preorderPrint(root.right)

    # 中序遍历
    def orderPrint(self, root: TreeNode) -> None:
        if not root:
            return
        self.orderPrint(root.left)
        print(root.val, end=' ')
        self.orderPrint(root.right)

    # 后序遍历
    def postorderPrint(self, root: TreeNode) -> None:
        if not root:
            return
        self.postorderPrint(root.left)
        self.postorderPrint(root.right)
        print(root.val, end=' ')

    # 层次遍历
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


nums = [3, 2, 3, None, 3, None, 1]
test = Solution()
root = test.constructBTree(nums)
test.levelorderPrint(root)
