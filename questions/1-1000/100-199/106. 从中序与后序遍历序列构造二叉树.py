import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

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


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
test = Solution()
root = test.buildTree(inorder, postorder)
test.levelorderPrint(root)
