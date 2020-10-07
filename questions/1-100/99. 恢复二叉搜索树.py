import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructTreeNodeDynamic(self, nums: list) -> TreeNode:
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

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def Trees(x): return [] if not x else Trees(
            x.left) + [x] + Trees(x.right)
        a = Trees(root)
        sa = sorted(a, key=lambda x: x.val)
        tmp = [a[i] for i in range(len(a)) if a[i] != sa[i]]
        tmp[0].val, tmp[1].val = tmp[1].val, tmp[0].val

    def preorderPrint(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preorderPrint(root.left)
        self.preorderPrint(root.right)


nums = [1, 3, None, None, 2]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
test.recoverTree(root)
test.preorderPrint(root)
print()
