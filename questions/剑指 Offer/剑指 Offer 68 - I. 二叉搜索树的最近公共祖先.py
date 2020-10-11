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

    # 迭代
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # 当前节点值比 p q 都小，说明 p q 都在右子树上
            if root.val < p.val and root.val < q.val:
                root = root.right
            # 当前节点值比 p q 都大，说明 p q 都在左子树上
            elif root.val > p.val and root.val > q.val:
                root = root.left
            # 当前节点小于等于 p q 中的一个节点，也大于等于 p q 中的另一个节点，就是他们的最近祖先节点
            else:
                break
        return root

    # 判断条件，思路与前面一致
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 确定 p.val > q.val 可以减少循环内的判断条件
        if p.val > q.val:
            p, q = q, p
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                break
        return root

    # 递归查找，思路一致
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root


nums = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p = TreeNode(2)
q = TreeNode(4)
test = Solution()
root = test.constructBTree(nums)
ancestor = test.lowestCommonAncestor(root, p, q)
print(ancestor.val)
