from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructTreeNodeDynamic(self, nums: list) -> TreeNode:
        q = deque()
        index = 0
        root = pre = TreeNode(nums[0])
        for i in range(1, len(nums)):
            if not nums[i]:
                if i > index * 2:
                    (pre, index) = q.popleft()
                continue
            cur = TreeNode(nums[i])
            if i % 2 == 1:
                pre.left = cur
                q.append((pre.left, i))
            else:
                pre.right = cur
                q.append((pre.right, i))
                (pre, index) = q.popleft()
        return root

    # 先序遍历
    def preorderPrint(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preorderPrint(root.left)
        self.preorderPrint(root.right)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def lnode(node): return not node.left and not node.right

        def dfs(node: TreeNode) -> int:
            ans = 0
            if node.left:
                ans += node.left.val if lnode(node.left) else dfs(node.left)
            if node.right and not lnode(node.right):
                ans += dfs(node.right)
            return ans
        return dfs(root) if root else 0


nums = [3, 9, 20, None, None, 15, 7]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
test.preorderPrint(root)
print(test.sumOfLeftLeaves(root))
